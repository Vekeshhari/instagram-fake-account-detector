def follower_following_ratio(followers: int, following: int):
    if following == 0:
        return None
    try:
        return round(followers / float(following), 2)
    except Exception:
        return None
