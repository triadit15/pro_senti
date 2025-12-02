import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Secret key from Render env
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev_key_fallback")

    # Database: Render provides DATABASE_URL for PostgreSQL
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL",
        "sqlite:///senti.db"  # fallback for local development
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Login manager setup
    login_manager = LoginManager()
    login_manager.login_view = "main.login"
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    from .marketplace_routes import market
    app.register_blueprint(market)

    from .utility_routes import utility
    app.register_blueprint(utility)

    return app