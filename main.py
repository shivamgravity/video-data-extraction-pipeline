import argparse
from pathlib import Path
from tqdm import tqdm

from src.logger import setup_logger
from src.config import load_config
from src.folders import get_next_folder
from src.pipeline import process_video

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Path to config JSON")
    parser.add_argument("--profile", help="Config profile name (dev, prod, test)")
    args = parser.parse_args()

    logger = setup_logger()
    config = load_config(args.config, args.profile)

    for url in tqdm(config["urls"], desc="Processing videos"):
        if config["folder_mode"] == "manual":
            name = input("Enter folder name: ")
            output_dir = Path("results") / name
        else:
            output_dir = get_next_folder()

        try:
            count = process_video(
                url,
                output_dir,
                config["interval"],
                logger
            )
            logger.info(f"Saved {count} frames → {output_dir}")
        except Exception:
            logger.exception("Video processing failed")

if __name__ == "__main__":
    main()
