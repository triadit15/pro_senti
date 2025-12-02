from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # -----------------------------
    # 🔐 SECRET KEY (FROM ENV)
    # -----------------------------
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "local_dev_key")

    # -----------------------------
    # 🗄 DATABASE SETUP
    # -----------------------------
    # Use Render DATABASE_URL if available
    database_url = os.environ.get("DATABASE_URL")

    if database_url:
        # Fix Render’s PostgreSQL URL format for SQLAlchemy
        database_url = database_url.replace("postgres://", "postgresql://")
        app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    else:
        # Local SQLite fallback
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///senti.db"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # -----------------------------
    # 🔐 LOGIN MANAGER
    # -----------------------------
    login_manager = LoginManager()
    login_manager.login_view = "main.login"
    login_manager.init_app(app)

    # Import User model so the loader works
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # -----------------------------
    # 🔗 BLUEPRINTS
    # -----------------------------
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    from .marketplace_routes import market
    app.register_blueprint(market)

    from .utility_routes import utility
    app.register_blueprint(utility)

    return app