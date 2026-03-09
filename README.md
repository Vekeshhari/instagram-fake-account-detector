Instagram Forensics (minimal)

This repository provides a minimal toolset to perform quick checks on Instagram profiles:
- Username heuristics
- Activity scoring
- Follower/following ratio
- Basic image forensics (metadata, ELA, simple clone detection)

Quick start

1. Create a virtual environment and install requirements:

```bash
python -m venv venv
venv\Scripts\activate    # Windows
pip install -r requirements.txt
Instagram Forensics (minimal)

This repository provides a minimal toolset to perform quick checks on Instagram profiles:
- Username heuristics
- Activity scoring
- Follower/following ratio
- Basic image forensics (metadata, ELA, simple clone detection)

Quick start

1. Create a virtual environment and install requirements:

```bash
python -m venv venv
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

2. Run the analyzer:

```bash
python main.py target_username
```

Notes
- `exiftool` (system binary) is optional; the scripts fall back to Pillow for EXIF extraction.
- Reverse image search must be done manually using the downloaded profile image (see reports/downloads).

Login for private profiles

- To analyze private or login-required profiles you must provide Instagram credentials. Set environment variables `INSTALOADER_USERNAME` and `INSTALOADER_PASSWORD` before running the script, for example on Windows PowerShell:

```powershell
$env:INSTALOADER_USERNAME = 'your_instagram_username'
$env:INSTALOADER_PASSWORD = 'your_password'
python project/main.py target_username
```

The script will attempt an automatic login when these environment variables are present.