# YT_2_mp3

A Python command-line tool for downloading YouTube videos as MP3 audio files.

## Features

- Downloads audio from YouTube videos and playlists
- Converts to MP3 format with configurable bitrate (128, 192, 256, or 320 kbps)
- Optionally embeds metadata including title, artist, and thumbnail artwork
- Supports custom output directory specification
- Includes retry logic for unstable network connections

## Requirements

- Python 3.x
- yt-dlp (`pip install yt-dlp`)
- ffmpeg (must be installed and available in system PATH)

## Usage
```bash
python yt_to_mp3.py <youtube_url> [options]
```

### Options

- `-o, --output-dir DIR` - Directory to save the MP3 file (default: current directory)
- `-q, --quality BITRATE` - Audio bitrate in kbps: 128, 192, 256, 320 (default: 192)
- `--no-metadata` - Skip embedding title, artist, and thumbnail metadata
- `-h, --help` - Display help message

### Examples
```bash
# Basic download
python yt_to_mp3.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Download with custom quality and output directory
python yt_to_mp3.py "https://youtu.be/dQw4w9WgXcQ" -o ~/Music -q 320

# Download without metadata
python yt_to_mp3.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --no-metadata
```

## How It Works

The script verifies required dependencies, downloads the best available audio stream from YouTube using yt-dlp, and converts it to MP3 format using ffmpeg. When metadata embedding is enabled, it also downloads the video thumbnail and embeds it as album artwork along with title and artist information.
