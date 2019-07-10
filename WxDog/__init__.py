from flask import Flask
from WxDog.blueprints.book import book
from WxDog.blueprints.author import author
from WxDog.blueprints.consumer import consumer
from WxDog.blueprints.rejump import rejump
from WxDog.blueprints.fileMgr import fileMgr
from WxDog.extensions import db, migrate, login_manager, bootstrap, dropzone, admin
from WxDog.models import Ebook, Chapter, Article
from WxDog import views


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    register_extensions(app)
    register_blueprints(app)
    register_setting(app)
    return app


def register_blueprints(app):
    app.register_blueprint(book, url_prefix='/book')
    app.register_blueprint(author, url_prefix='/author')
    app.register_blueprint(consumer, url_prefix='/consumer')
    app.register_blueprint(rejump, url_prefix='/')
    app.register_blueprint(fileMgr, url_prefix='/fileMgr')


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    dropzone.init_app(app)
    admin.init_app(app)


def register_setting(app):
    app.jinja_env.variable_start_string = '[['
    app.jinja_env.variable_end_string = ']]'