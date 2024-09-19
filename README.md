# Youtube_Video_Downloader
A Youtube Video Downloader using Python

# YouTube Downloader with Format Selection

This Python script allows you to download YouTube videos with custom video and audio quality options. It uses yt-dlp for downloading and ffmpeg for merging video and audio streams.

## Features

- List available video and audio formats for a given YouTube URL
- Select specific video and audio quality
- Download video and audio separately
- Merge video and audio into a single file
- Display download progress
- Handle filenames with special characters

## Requirements

- Python 3.6 or higher
- yt-dlp
- ffmpeg

## Installation

1. Ensure you have Python 3.6 or higher installed on your system.

2. Install the required Python library:

   ```
   pip install yt-dlp
   ```

3. Install ffmpeg:
   - On Windows:
     - Download ffmpeg from the official website: https://ffmpeg.org/download.html
     - Extract the downloaded archive
     - Add the bin folder to your system's PATH environment variable
   - On macOS (using Homebrew):
     ```
     brew install ffmpeg
     ```
   - On Ubuntu or Debian:
     ```
     sudo apt update
     sudo apt install ffmpeg
     ```

4. Download the `youtube_downloader.py` script to your local machine.

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory containing the `youtube_downloader.py` script.

3. Run the script using Python:

   ```
   python youtube_downloader.py
   ```

4. When prompted, enter the YouTube video URL.

5. Choose the desired video quality from the list of available formats.

6. Choose the desired audio quality from the list of available formats.

7. The script will download the video and audio, then merge them into a single file.

8. The merged file will be saved in the specified output directory (default is "D:/youtube_download").

## Customization

You can modify the following variables in the script:

- `url`: The YouTube video URL to download
- `save_path`: The directory where downloaded files will be saved

## Troubleshooting

If you encounter any issues:

1. Ensure all requirements are correctly installed.
2. Check that ffmpeg is properly installed and accessible from the command line.
3. Verify that you have write permissions in the specified save directory.
4. If you're having problems with a specific video, try another URL to see if the issue persists.

## License

This script is provided "as is", without warranty of any kind. Use at your own risk.

## Disclaimer

This script is for personal use only. Respect copyright laws and YouTube's terms of service when using this tool.
