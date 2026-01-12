import subprocess
from pathlib import Path

def extract_frames_ffmpeg(video_path, output_dir, interval, logger):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if interval == -1:
        vf = "fps=source_fps"
    else:
        vf = f"fps=1/{interval}"

    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel", "error",
        "-i", str(video_path),
        "-vf", vf,
        "-q:v", "2",
        str(output_dir / "frame_%06d.jpg")
    ]

    logger.info("Extracting frames with FFmpeg...")
    subprocess.run(cmd, check=True)

    count = len(list(output_dir.glob("frame_*.jpg")))
    logger.info(f"Extracted {count} frames")
    return count
