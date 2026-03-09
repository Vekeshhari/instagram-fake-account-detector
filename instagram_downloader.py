import os
import time
import instaloader


def download_images(username, base_dir):

    outdir = os.path.join(base_dir, "downloads")
    os.makedirs(outdir, exist_ok=True)

    L = instaloader.Instaloader(
        dirname_pattern=os.path.join(outdir, "{profile}"),
        download_videos=False,
        download_video_thumbnails=False,
        save_metadata=False
    )

    try:
        profile = instaloader.Profile.from_username(L.context, username)
    except Exception as e:
        print("Profile fetch failed:", e)
        return None, None

    try:
        # download profile pic
        L.download_profile(profile.username, profile_pic_only=True)

        time.sleep(5)

        # download posts (limit to avoid rate limit)
        for i, post in enumerate(profile.get_posts()):

            if i >= 7:
                break

            try:
                L.download_post(post, target=profile.username)
            except Exception as e:
                print("Post download failed:", e)

            time.sleep(10)

        return profile, os.path.join(outdir, profile.username)

    except Exception as e:
        print("Download error:", e)
        return None, None