import shutil
from src.downloader import download_video
from src.ffmpeg_utils import extract_frames_ffmpeg

def process_video(url, output_dir, interval, logger):
    video_path, temp_dir = download_video(url, logger)
    count = extract_frames_ffmpeg(video_path, output_dir, interval, logger)
    shutil.rmtree(temp_dir)
    logger.info("Temporary files cleaned up")
    return count
