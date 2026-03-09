def activity_score(posts: int, followers: int) -> dict:
    if followers == 0:
        return {"score": 0.0, "classification": "Suspicious (0 followers)"}
    ratio = posts / float(followers)
    if ratio < 0.001:
        return {"score": round(ratio, 6), "classification": "Low activity"}
    if ratio > 0.5:
        return {"score": round(ratio, 6), "classification": "High posting relative to followers (possible automation)"}
    return {"score": round(ratio, 6), "classification": "Normal"}
