from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    """Construct the core app object."""
    app = Flask(__name__)

    # Application Configuration
    app.config.from_pyfile("config.py")

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)

    # register all blueprints
    from .views import blueprints

    for bp in blueprints:
        app.register_blueprint(bp)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    return app


app = create_app()
