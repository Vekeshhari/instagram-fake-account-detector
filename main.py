import argparse
import json
import os

from downloader.instagram_downloader import download_images
from profile_analysis.username_check import suspicious_username
from profile_analysis.activity_analysis import activity_score
from profile_analysis.account_features import extract_account_features
from follower_analysis.ratio_analysis import follower_following_ratio
from image_forensics.image_pipeline import analyze_images
from reverse_search.tineye_stub import reverse_search_hint
from decision_engine import ensemble_score


BASE_DIR = os.path.dirname(__file__)


def analyze(username):

    # Download profile and images
    profile, folder = download_images(username, BASE_DIR)

    if profile is None or folder is None:
        return {"error": "Failed to fetch Instagram profile"}

    report = {
        "username": username
    }

    # Username pattern check
    report["username_suspicious"] = suspicious_username(profile.username)

    # Activity analysis
    report["activity"] = activity_score(
        profile.mediacount,
        profile.followers
    )

    # Follower ratio
    report["follower_ratio"] = follower_following_ratio(
        profile.followers,
        profile.followees
    )

    # Extract account behaviour features
    account_features = extract_account_features(profile)

    report["account_features"] = account_features

    # Image forensic analysis
    image_results = analyze_images(folder)

    if image_results is None:
        image_results = []

    report["image_results"] = image_results

    # Reverse search hint
    report["reverse_search_hint"] = reverse_search_hint()

    # Risk scoring
    report["risk_assessment"] = ensemble_score(
        account_features,
        image_results
    )

    return report


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Instagram Forensic Analyzer"
    )

    parser.add_argument(
        "username",
        help="Instagram username to analyze"
    )

    args = parser.parse_args()

    result = analyze(args.username)

    print(json.dumps(result, indent=2))