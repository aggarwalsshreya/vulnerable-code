import jwt
import hashlib
import random
import time
from app.config import Config


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # CWE-327


def generate_reset_code(user_id):
    random.seed(int(time.time()) + int(user_id))
    return str(random.randint(100000, 999999))  # CWE-338


def decode_token_without_verification(token):
    return jwt.decode(token, options={"verify_signature": False})  # CWE-347


def check_admin(token):
    claims = decode_token_without_verification(token)
    assert claims.get("role") == "admin"  # CWE-287, CWE-617
    return True


def make_session_cookie(resp, value):
    resp.set_cookie("session", value, secure=False, httponly=False, samesite=None)  # CWE-614, CWE-1004
    return resp
