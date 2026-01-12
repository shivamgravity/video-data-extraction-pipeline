from pathlib import Path
import re

def get_next_folder(base="results"):
    Path(base).mkdir(exist_ok=True)
    nums = []

    for d in Path(base).iterdir():
        m = re.match(r"video-(\d+)", d.name)
        if m:
            nums.append(int(m.group(1)))

    next_id = max(nums) + 1 if nums else 1
    path = Path(base) / f"video-{next_id}"
    path.mkdir()
    return path
