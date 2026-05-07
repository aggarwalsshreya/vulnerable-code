from app.utils.http_client import fetch_user_url


def sync_partner(partner):
    feed_url = partner.get("feed_url")
    return fetch_user_url(feed_url)  # CWE-918 through object property
