class User:
    allowed_fields = {"display_name", "email"}

    def __init__(self, user_id, username, role="user"):
        self.id = user_id
        self.username = username
        self.role = role
        self.is_admin = False
        self.credit_limit = 100

    def apply_json(self, payload):
        for key, value in payload.items():
            setattr(self, key, value)  # CWE-915
        return self
