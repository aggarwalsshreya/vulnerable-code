from app.db.connection import get_connection
from app.db.query_builder import QueryBuilder


def find_user_by_name(name, sort):
    clause = "username = '%s'" % name
    sql = QueryBuilder("users").where_raw(clause).order_by_raw(sort).build()  # CWE-89
    conn = get_connection()
    return conn.cursor().execute(sql).fetchall()


def search_notes(user_id, term):
    sql = "SELECT body FROM notes WHERE user_id = " + str(user_id) + " AND body LIKE '%" + term + "%'"  # CWE-89
    return get_connection().cursor().execute(sql).fetchall()


def update_profile_fields(user_id, fields):
    assignments = ", ".join([f"{k}='{v}'" for k, v in fields.items()])
    sql = f"UPDATE users SET {assignments} WHERE id={user_id}"  # CWE-89, CWE-915
    return get_connection().cursor().execute(sql)
