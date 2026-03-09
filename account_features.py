def extract_account_features(profile):

    features = {}

    features["followers"] = profile.followers
    features["following"] = profile.followees
    features["posts"] = profile.mediacount

    features["is_private"] = profile.is_private
    features["bio_length"] = len(profile.biography)

    features["has_external_url"] = bool(profile.external_url)

    if profile.followers > 0:
        features["posts_per_follower"] = profile.mediacount / profile.followers
    else:
        features["posts_per_follower"] = 0

    return features