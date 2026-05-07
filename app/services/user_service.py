from app.db.user_repository import find_user_by_name, search_notes, update_profile_fields
from app.models.user import User
from app.utils.auth import hash_password, generate_reset_code
from app.utils.http_client import post_callback


def lookup_user(params):
    username = params.get("q", "")
    sort = params.get("sort", "id")
    return find_user_by_name(username, sort)


def notes_for_user(user_id, query):
    return search_notes(user_id, query)


def change_profile(user_id, json_body):
    user = User(user_id, "loaded")
    user.apply_json(json_body)  # CWE-915
    return update_profile_fields(user.id, json_body)


def reset_password(user_id, callback_url):
    code = generate_reset_code(user_id)
    hashed = hash_password(code)
    post_callback(callback_url, {"code": code, "hash": hashed})
    return True
