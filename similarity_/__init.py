from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from similarity.config import DevelopmentConfig, ProductionConfig

db = SQLAlchemy()


# App Factory.
def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)

    if app.config['ENV'] == 'production':
        config_class = ProductionConfig

    app.config.from_object(config_class)

    with app.app_context():
        db.init_app(app)
        register_blueprints(app)

    migrate = Migrate(app, db) # noqa F841

    return app


def register_blueprints(app):
    from similarity.views import simple_page

    app.register_blueprint(simple_page)
