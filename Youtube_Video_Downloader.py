import yt_dlp
import subprocess
import os
import re

def get_size_in_mb(size):
    """Convert file size from bytes to MB."""
    if size is None:
        return "Unknown"
    return round(size / (1024 * 1024), 2)  # Convert bytes to MB

def sanitize_filename(filename):
    """Remove special characters from file names."""
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def list_formats(formats, media_type):
    """List available formats with size information."""
    print(f"\nAvailable {media_type} formats:")
    for idx, fmt in enumerate(formats):
        resolution = fmt.get('height', 'N/A') if media_type == 'video' else 'N/A'
        bitrate = fmt.get('tbr', 'N/A') if media_type == 'video' else fmt.get('abr', 'N/A')
        size_mb = get_size_in_mb(fmt.get('filesize'))
        print(f"{idx + 1}. {fmt['format_id']} - Resolution: {resolution}, Bitrate: {bitrate} kbps, Size: {size_mb} MB")

def download_and_merge(url, save_path):
    try:
        # Fetch available formats
        ydl_opts_list = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
            'quiet': True,
            'dumpjson': True
        }

        with yt_dlp.YoutubeDL(ydl_opts_list) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_formats = [fmt for fmt in info_dict.get('formats', []) if fmt.get('vcodec') != 'none']
            audio_formats = [fmt for fmt in info_dict.get('formats', []) if fmt.get('acodec') != 'none']
            
            if not video_formats or not audio_formats:
                print("No valid video or audio formats found.")
                return

            # List video formats
            list_formats(video_formats, 'video')
            video_choice = int(input("Choose video quality (number): ")) - 1
            if video_choice < 0 or video_choice >= len(video_formats):
                print("Invalid choice.")
                return

            # List audio formats
            list_formats(audio_formats, 'audio')
            audio_choice = int(input("Choose audio quality (number): ")) - 1
            if audio_choice < 0 or audio_choice >= len(audio_formats):
                print("Invalid choice.")
                return

            selected_video_format = video_formats[video_choice]
            selected_audio_format = audio_formats[audio_choice]

            # Sanitize title and create file paths
            sanitized_title = sanitize_filename(info_dict['title'])
            output_file = os.path.join(save_path, f"{sanitized_title}_merged.mp4")

            # Download selected formats
            ydl_opts_download = {
                'outtmpl': os.path.join(save_path, f'{sanitized_title}.%(ext)s'),
                'format': f"{selected_video_format['format_id']}+{selected_audio_format['format_id']}",
                'noplaylist': True,
                'progress_hooks': [print_progress],
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }],
                'merge_output_format': 'mp4'
            }

            print(f"\nDownloading and merging video and audio...")
            with yt_dlp.YoutubeDL(ydl_opts_download) as ydl:
                ydl.download([url])

            print(f"Download and merge completed. File saved as: {output_file}")

    except Exception as e:
        print(f"Error: {e}")

def print_progress(d):
    """Print download progress."""
    if d['status'] == 'downloading':
        print(f"\rDownloading: {d['_percent_str']} of {d['_total_bytes_str']}", end='')
    elif d['status'] == 'finished':
        print(f"\nDone downloading: {d['filename']}")

# Example usage
url = "https://www.youtube.com/watch?v=PJWemSzExXs"
save_path = "D:/youtube_download"

download_and_merge(url, save_path)
