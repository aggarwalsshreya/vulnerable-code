from flask import Flask
from app.api.user_routes import user_bp
from app.api.admin_routes import admin_bp
from app.api.file_routes import file_bp
from app.api.webhook_routes import webhook_bp
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(file_bp, url_prefix="/files")
    app.register_blueprint(webhook_bp, url_prefix="/hooks")
    return app
