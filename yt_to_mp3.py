#!/usr/bin/env python3
#########################
# author:  4x0r-b17     #
# name:    yt_to_mp3.py #
# version: 1.0          #
#########################

import argparse
import os
import sys

# verify yt-dlp and ffmpeg are available before running
def check_dependencies():
    import shutil

    missing = []

    try:
        import yt_dlp
    except ImportError:
        missing.append("yt-dlp  →  pip install yt-dlp")

    if not shutil.which("ffmpeg"):
        missing.append("ffmpeg  →  https://ffmpeg.org/download.html")

    if missing:
        print("[x] missing dependencies:")
        for dep in missing:
            print(f"   • {dep}")
        sys.exit(1)

def parse_args():
    parser = argparse.ArgumentParser(
        description="Download a YouTube URL as an MP3 file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("url", help="YouTube video or playlist URL")
    parser.add_argument(
        "-o", "--output-dir",
        default=".",
        metavar="DIR",
        help="Directory to save the MP3 file(s) (default: current directory)",
    )
    parser.add_argument(
        "-q", "--quality",
        default="192",
        choices=["128", "192", "256", "320"],
        metavar="BITRATE",
        help="Audio bitrate in kbps: 128, 192, 256, 320 (default: 192)",
    )
    parser.add_argument(
        "--no-metadata",
        action="store_true",
        help="Skip embedding title, artist, and thumbnail metadata into the MP3",
    )
    return parser.parse_args()

# build the yt-dlp options dictionary
def build_ydl_options(output_dir: str, quality: str, embed_metadata: bool) -> dict:
    output_template = os.path.join(output_dir, "%(title)s.%(ext)s")

    postprocessors = [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": quality,
        }
    ]

    if embed_metadata:
        postprocessors += [
            {"key": "FFmpegMetadata", "add_metadata": True},
            {"key": "EmbedThumbnail"},
        ]

    return {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "postprocessors": postprocessors,
        "writethumbnail": embed_metadata,
        "quiet": False,
        "no_warnings": False,
        "retries": 3,
        "fragment_retries": 3,
    }

def download(url: str, output_dir: str, quality: str, embed_metadata: bool):
    import yt_dlp

    os.makedirs(output_dir, exist_ok=True)

    options = build_ydl_options(output_dir, quality, embed_metadata)

    print(f"[-]  Downloading: {url}")
    print(f"[-]  Output dir : {os.path.abspath(output_dir)}")
    print(f"[-]  Bitrate    : {quality} kbps")
    print(f"[-]  Metadata   : {'yes' if embed_metadata else 'no'}\n")

    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            info = ydl.extract_info(url, download=True)
            # Playlists return a list; single videos return a dict
            entries = info.get("entries", [info]) if info else []
            count = len(entries) if entries else 1
            print(f"\n[v] Done! {count} file(s) saved to: {os.path.abspath(output_dir)}")
        except yt_dlp.utils.DownloadError as e:
            print(f"\n[x] Download failed: {e}", file=sys.stderr)
            sys.exit(1)


def main():
    args = parse_args()
    check_dependencies()
    download(
        url=args.url,
        output_dir=args.output_dir,
        quality=args.quality,
        embed_metadata=not args.no_metadata,
    )


if __name__ == "__main__":
    main()
