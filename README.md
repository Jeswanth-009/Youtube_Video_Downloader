# Youtube_Video_Downloader
A Youtube Video Downloader using Python

# YouTube Downloader Script

## Overview
This Python script allows users to download YouTube videos with separate audio and video streams, and then merge them into a single MP4 file. It provides options to choose video and audio quality before downloading.

## Features
- Lists available video and audio formats for a given YouTube URL
- Allows user to select desired video and audio quality
- Downloads and merges selected formats into a single MP4 file
- Displays download progress in real-time
- Handles errors gracefully, including cases where file size information is not available

## Requirements
- Python 3.6+
- yt-dlp library
- FFmpeg (must be installed and accessible in system PATH)

## Installation
1. Ensure you have Python 3.6 or higher installed.
2. Install the required library:
   ```
   pip install yt-dlp
   ```
3. Install FFmpeg and make sure it's in your system PATH.

## Usage
1. Run the script:
   ```
   python youtube_downloader.py
   ```
2. When prompted, enter the YouTube URL of the video you want to download.
3. Choose the desired video quality from the list of available formats.
4. Choose the desired audio quality from the list of available formats.
5. The script will download and merge the selected video and audio into a single MP4 file.

## Main Functions

### `get_size_in_mb(size)`
Converts file size from bytes to megabytes. Returns "Unknown" if size is None.

### `sanitize_filename(filename)`
Removes special characters from filenames to ensure compatibility with file systems.

### `list_formats(formats, media_type)`
Displays available video or audio formats with their quality and size information.

### `download_and_merge(url, save_path)`
Main function that handles the download and merging process. It fetches available formats, prompts user for quality selection, and then downloads and merges the selected formats.

### `print_progress(d)`
Callback function to display download progress in real-time.

## Error Handling
The script includes error handling to manage common issues such as:
- Invalid user input
- Network errors
- Missing file size information

## Customization
You can modify the `save_path` variable in the script to change the default download location.

## Limitations
- This script is intended for personal use only. Respect copyright laws and YouTube's terms of service.
- Some videos may not be available for download due to restrictions set by the content creator or YouTube.

## Troubleshooting
If you encounter any issues:
1. Ensure all dependencies are correctly installed.
2. Check that FFmpeg is properly installed and accessible in your system PATH.
3. Verify that you have a stable internet connection.
4. Make sure you have write permissions in the specified save directory.

## Disclaimer
This script is for educational purposes only. Users are responsible for complying with all applicable laws and terms of service.
