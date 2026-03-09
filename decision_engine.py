def calculate_risk(report):

    score = 0

    # Username suspicious
    if report.get("username_suspicious"):
        score += 20

    # Activity check
    activity = report.get("activity", {})
    classification = activity.get("classification", "").lower()

    if "low activity" in classification:
        score += 20
    elif "automation" in classification:
        score += 30

    # Follower ratio
    ratio = report.get("follower_ratio")

    if ratio is not None and ratio < 0.1:
        score += 20

    # Clone detection
    clone = report.get("clone_score")

    if clone and clone > 0.85:
        score += 20

    # Metadata missing
    if not report.get("metadata_found"):
        score += 10

    score = min(score, 100)

    if score >= 70:
        level = "HIGH RISK"
    elif score >= 40:
        level = "MEDIUM RISK"
    else:
        level = "LOW RISK"

    return {
        "risk_score": score,
        "risk_level": level
    }


def ensemble_score(account, images):

    score = 0

    # Account behaviour
    if account.get("posts", 0) < 3:
        score += 10

    if account.get("bio_length", 0) < 3:
        score += 5

    if account.get("has_external_url"):
        score += 10

    if account.get("posts_per_follower", 0) < 0.001:
        score += 10

    suspicious_images = 0

    for img in images:

        clone_score = img.get("clone_score")
        ai_score = img.get("ai_face_score")

        if clone_score and clone_score > 0.9:
            suspicious_images += 1

        if ai_score and ai_score > 0.4:
            suspicious_images += 1

    total_images = len(images)

    if total_images > 0:

        suspicious_ratio = suspicious_images / total_images

        if suspicious_ratio > 0.6:
            score += 40
        elif suspicious_ratio > 0.3:
            score += 20
        elif suspicious_ratio > 0.1:
            score += 10

    score = min(score, 100)

    if score >= 70:
        level = "HIGH RISK"
    elif score >= 40:
        level = "MEDIUM RISK"
    else:
        level = "LOW RISK"

    return {
        "risk_score": score,
        "risk_level": level
    }