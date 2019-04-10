from flask import Flask
from WxDog.blueprints.book import book
from WxDog.extensions import db, migrate, admin
from WxDog.models import Ebook, Chapter, Article
from WxDog import views


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    register_extensions(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(book, url_prefix='/book')


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
