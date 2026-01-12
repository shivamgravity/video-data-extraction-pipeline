# Video Data Extraction Pipeline

A **production-ready Python pipeline** to download YouTube videos and extract frames at user-defined intervals using **yt-dlp** and **FFmpeg**.

This project is designed for:
- Dataset creation
- Computer vision preprocessing
- Research workflows
- Batch video frame extraction

It supports **interactive mode**, **JSON configuration**, and **multiple config profiles** (dev / test / prod).

---

## ✨ Features

- ⏱️ Extract frames at a fixed interval (e.g. every 1s, 5s)
- 🔁 Extract **all frames** with `interval = -1`
- 🎥 Supports **single** and **batch** video processing
- 📐 Automatically downloads **1080p if available**, else best quality
- 🧹 Cleans up downloaded videos after extraction
- 📁 Auto or manual output folder naming
- 📄 JSON config support for reproducibility
- 🧪 Multiple config profiles (`dev`, `test`, `prod`)
- 📊 Progress bars for batch processing
- 🧾 Structured logging (file + console)
- ⚡ Fast, reliable frame extraction using **FFmpeg**

---

## 🧠 Why FFmpeg (not OpenCV)?

This project intentionally uses **FFmpeg** instead of OpenCV for frame extraction because:

- Faster and more reliable
- Excellent codec support
- Accurate FPS handling
- Industry-standard for media pipelines

OpenCV can be added later for **post-processing**, not extraction.

---

## 📁 Project Structure

video-data-extraction-pipeline/
│
├── src/
│ ├── init.py
│ ├── config.py # Config & profile loading
│ ├── logger.py # Logging setup
│ ├── downloader.py # yt-dlp integration
│ ├── ffmpeg_utils.py # FFmpeg frame extraction
│ ├── folders.py # Folder naming logic
│ └── pipeline.py # Orchestration
│
├── configs/
│ ├── config.dev.json
│ ├── config.test.json
│ └── config.prod.json
│
├── results/ # Extracted frames (gitignored)
├── logs/ # Log files (gitignored)
├── main.py # Entry point
├── requirements.txt
├── .gitignore
└── README.md

---

## 🛠️ Requirements

### Python
- Python **3.9+**

### Python Dependencies
Install with:
```bash
pip install -r requirements.txt
```

### System Dependency (Required)
* **FFmpeg**

**Install FFmpeg**
* **Windows:** [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
* **Linux:**
    ```bash
    sudo apt install ffmpeg
    ```
* **macOS:**
    ```bash
    brew install ffmpeg
    ```

Verify:
    ```bash
    ffmpeg -version
    ```

## Usage

### Interactive Mode

```bash
python main.py
```

You will be prompted for:
* Frame Interval
* Single / batch mode
* Folder naming mode
* Video URLs

### Using a Config Profile

```bash
python main.py --profile test
```

Loads:
```arduino
configs/config.test.json
```

### Using a Custom Config File

```bash
python main.py --config my_config.json
```

#### Config File Format

Example: `configs/config.test.json`

```json
{
    "interval":10,
    "mode": "single",
    "folder_mode": "auto",
    "urls" [
        "https://www.youtube.com/watch?v=VIDEO_ID"
    ]
}
```

#### Config Options

| Key | Description |
|-----|-------------|
| `interval` | Seconds between frames (`-1` = all frames) |
| `mode` | `single` or `batch` |
| `folder_mode` | `manual` or `auto` |
| `urls` | List of YouTube URLs |

## Output

Frames are saved as:

```css
results/
└── video-3/
    ├── frame_000001.jpg
    ├── frame_000002.jpg
    └── ...
```

Downloaded videos are **automatically deleted** after extraction.

## Logging

* Logs are written to:
    ```bash
    logs/app.log
    ```
* Logs include:
    * Download status
    * Frame extraction progress
    * Errors and stack traces

Logs are **ASCII-safe** for Windows compatibility.

## Future Enhancements

* Resume / skip already proecssed videos
* CLI flags for overrides
* Dependecy auto-check (`ffmpeg`, `ndoe`)
* Docker support
* Post-processing hooks (OpenCV optional)
* Unit tests

## License
MIT License.