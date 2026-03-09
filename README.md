# Instagram Forensics

A digital forensic tool for analyzing Instagram profiles to detect
suspicious or potentially fake accounts using behavioral analysis and
image forensics.

------------------------------------------------------------------------

## Features

The tool performs several checks on Instagram profiles:

-   Username heuristic analysis
-   Activity scoring
-   Follower / following ratio analysis
-   Account behaviour analysis
-   Image forensic analysis
    -   Metadata extraction
    -   Error Level Analysis (ELA)
    -   Clone detection
    -   Noise inconsistency detection
    -   AI-generated face indicators
-   Automated risk scoring
-   JSON and PDF forensic report generation
-   Graphical User Interface for interactive investigation

------------------------------------------------------------------------

## Quick Start

### 1. Create Virtual Environment

``` bash
python -m venv venv
```

Activate environment:

Windows

``` bash
venv\Scripts\activate
```

Linux / Mac

``` bash
source venv/bin/activate
```

------------------------------------------------------------------------

### 2. Install Requirements

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Usage

### Command Line Mode

Run the analyzer from the terminal:

``` bash
python main.py target_username
```

Example:

``` bash
python main.py nasa
```

The tool will:

1.  Fetch Instagram profile data
2.  Download profile image and posts
3.  Perform forensic analysis
4.  Generate a risk score
5.  Create JSON and PDF investigation reports

------------------------------------------------------------------------

### GUI Mode

You can also run the graphical interface:

``` bash
python gui.py
```

Steps:

1.  Launch the application
2.  Enter an Instagram username
3.  Click **Start Investigation**
4.  View the forensic analysis report

The GUI displays:

-   Account analysis results
-   Image forensic indicators
-   Risk score and risk level
-   Generated forensic evidence images

------------------------------------------------------------------------

## Output

Reports are generated inside the **reports** folder:

reports/ ├── report.json ├── forensic_report.pdf └── ela_image.jpg

Example result:

Username: example_account

Risk Score: 18\
Risk Level: LOW RISK\
Fake Account Probability: 18%

------------------------------------------------------------------------

## Login for Private Profiles

To analyze private or login-required profiles, provide Instagram
credentials using environment variables.

Windows PowerShell:

``` powershell
$env:INSTALOADER_USERNAME="your_instagram_username"
$env:INSTALOADER_PASSWORD="your_password"
```

Then run:

``` bash
python main.py target_username
```

The script will automatically attempt login using Instaloader.

------------------------------------------------------------------------

## Notes

-   `exiftool` is optional but recommended for full metadata extraction.
-   Reverse image search must be performed manually using downloaded
    images.
-   Instagram rate limits may temporarily block requests if too many
    profiles are analyzed quickly.

------------------------------------------------------------------------

## Project Structure

instagram-forensics
│
├── main.py                # Command line analyzer
├── gui.py                 # Graphical interface
├── decision_engine.py     # Risk scoring system
|
│
├── downloader
│   └── instagram_downloader.py
│
├── profile_analysis
│   ├── username_check.py
│   ├── activity_analysis.py
│   └── account_features.py
│
├── follower_analysis
│   └── ratio_analysis.py
│
├── image_forensics
│   ├── jpeg_analysis.py
│   ├── metadata.py
│   ├── pixel_analysis.py
│   ├── advanced_forensics.py
│   ├── ai_face_detection.py
│   └── image_pipeline.py
│
├── reverse_search
│   └── tineye_stub.py
│
├── downloads


------------------------------------------------------------------------

## Disclaimer

This project is intended for **educational and research purposes only**.

The risk score indicates a **probability of suspicious behaviour**, not
definitive proof that an account is fake.
