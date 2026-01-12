import json
from pathlib import Path

DEFAULT_CONFIG = {
    "interval": 1,
    "mode": "single",
    "folder_mode": "auto",
    "urls": []
}

def load_config(config_path=None, profile=None):
    if profile:
        config_path = Path("configs") / f"config.{profile}.json"

    if config_path:
        if not Path(config_path).exists():
            raise FileNotFoundError(f"Config not found: {config_path}")

        with open(config_path, "r") as f:
            user_config = json.load(f)

        return {**DEFAULT_CONFIG, **user_config}

    return interactive_config()


def interactive_config():
    interval = int(input("Frame interval in seconds (-1 = all frames): "))
    mode = input("Mode (single / batch): ").strip().lower()
    folder_mode = input("Folder mode (manual / auto): ").strip().lower()

    urls = []
    if mode == "single":
        urls.append(input("Enter YouTube URL: "))
    else:
        n = int(input("Number of videos: "))
        urls = [input(f"URL {i+1}: ") for i in range(n)]

    return {
        "interval": interval,
        "mode": mode,
        "folder_mode": folder_mode,
        "urls": urls
    }
