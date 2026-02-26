# YT_2_mp3

![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey?style=flat-square)
![Interface](https://img.shields.io/badge/Interface-CLI-orange?style=flat-square)
![Dependencies](https://img.shields.io/badge/Requires-yt--dlp%20%7C%20ffmpeg-green?style=flat-square)

A Python command-line tool for downloading YouTube videos and playlists as MP3 audio files, with configurable quality, metadata embedding, and retry logic for unstable connections.

---

## Features

- Downloads audio from YouTube videos and playlists via `yt-dlp`
- Converts to MP3 with selectable bitrate — 128, 192, 256, or 320 kbps
- Optionally embeds metadata including title, artist, and thumbnail as album artwork
- Supports custom output directory specification
- Includes retry logic for unstable network connections

---

## Requirements

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-red?style=flat-square)
![ffmpeg](https://img.shields.io/badge/ffmpeg-system%20PATH-darkgreen?style=flat-square)

- Python 3.x
- `yt-dlp` — `pip install yt-dlp`
- `ffmpeg` — must be installed and available in system PATH

---

## Usage

```bash
python yt_to_mp3.py <youtube_url> [options]
```

### Options

| Flag | Description | Default |
|---|---|---|
| `-o, --output-dir DIR` | Directory to save the MP3 file | Current directory |
| `-q, --quality BITRATE` | Audio bitrate in kbps: 128, 192, 256, 320 | 192 |
| `--no-metadata` | Skip embedding title, artist, and thumbnail | Enabled |
| `-h, --help` | Display help message | — |

### Examples

```bash
# Basic download
python yt_to_mp3.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Download with custom quality and output directory
python yt_to_mp3.py "https://youtu.be/dQw4w9WgXcQ" -o ~/Music -q 320

# Download without metadata
python yt_to_mp3.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --no-metadata
```

---

## How It Works

The script verifies required dependencies on startup, then uses `yt-dlp` to fetch the best available audio stream from the provided URL. The stream is passed to `ffmpeg` for conversion to MP3 at the specified bitrate. When metadata embedding is enabled, the video thumbnail is downloaded separately and embedded as album artwork alongside title and artist information.

---

## Skills Demonstrated

![Python](https://img.shields.io/badge/Skill-CLI%20Tool%20Development-blue?style=flat-square)
![Audio](https://img.shields.io/badge/Skill-Audio%20Processing%20%26%20Conversion-purple?style=flat-square)
![Automation](https://img.shields.io/badge/Skill-Process%20Automation-orange?style=flat-square)
![Metadata](https://img.shields.io/badge/Skill-Metadata%20%26%20File%20Handling-green?style=flat-square)

- CLI tool design with `argparse` — flags, defaults, and help documentation
- Subprocess management — spawning and controlling `ffmpeg` from Python
- External API interaction — audio extraction via `yt-dlp`
- File and metadata handling — embedding artwork and tags into MP3 containers
- Resilience patterns — dependency validation and network retry logic
