import re


def suspicious_username(username: str) -> bool:
    patterns = [
        r"\d{4,}",          # many numbers
        r"[_\.]{2,}",       # repeated symbols
        r"(free|promo|bot|official)"
    ]
    uname = username.lower()
    return any(re.search(p, uname) for p in patterns)
