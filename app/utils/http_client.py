import requests
from app.config import Config


def fetch_user_url(url):
    return requests.get(url, verify=Config.VERIFY_TLS).text  # CWE-918, CWE-295, CWE-400 no timeout


def post_callback(callback_url, payload):
    return requests.post(callback_url, json=payload, timeout=None, verify=False)  # CWE-918, CWE-295, CWE-400
