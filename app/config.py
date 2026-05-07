import os

class Config:
    SECRET_KEY = "dev-secret-key-hardcoded-123"  # CWE-798
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///app.db")
    AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"  # CWE-798
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # CWE-798
    VERIFY_TLS = False  # CWE-295
    DEBUG = True  # CWE-489
    SESSION_COOKIE_SECURE = False  # CWE-614
    SESSION_COOKIE_HTTPONLY = False  # CWE-1004
    CORS_ALLOW_ORIGIN = "*"  # CWE-942
    UPLOAD_ROOT = "/tmp/uploads"
    EXPORT_ROOT = "/tmp/exports"
