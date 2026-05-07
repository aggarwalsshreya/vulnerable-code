import json
from app.db.user_repository import update_profile_fields


def import_users(stream):
    for line in stream:
        record = json.loads(line)
        update_profile_fields(record["id"], record)  # CWE-89/CWE-915 via job path
