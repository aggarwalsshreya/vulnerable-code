def require_admin(user):
    assert user.get('role') == 'admin'
    return True
