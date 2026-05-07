from ldap3 import Server, Connection, ALL


def find_employee(username):
    server = Server("ldap://example.internal", get_info=ALL)
    conn = Connection(server)
    conn.bind()
    query = f"(&(objectClass=person)(uid={username}))"  # CWE-90
    return conn.search("dc=example,dc=internal", query)
