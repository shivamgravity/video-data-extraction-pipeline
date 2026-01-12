import yt_dlp
import tempfile
import os
from pathlib import Path

def download_video(url, logger):
    temp_dir = tempfile.mkdtemp()

    ydl_opts = {
        "format": "bv*[height<=1080]+ba/best",
        "merge_output_format": "mp4",
        "outtmpl": os.path.join(temp_dir, "%(title)s.%(ext)s"),
        "quiet": True,
    }

    logger.info("Downloading video...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url, download=True)

    video_file = next(
        Path(temp_dir).glob("*.mp4")
    )

    logger.info(f"Downloaded to {video_file.name}")
    return video_file, temp_dir
