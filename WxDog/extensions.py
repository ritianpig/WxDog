from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_dropzone import Dropzone
from flask_admin import Admin


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bootstrap = Bootstrap()
dropzone = Dropzone()
admin = Admin(template_mode='bootstrap3')


@login_manager.user_loader
def load_user(user_id):
    from WxDog.models import AdminLogin
    user = AdminLogin.query.get(int(user_id))
    return user


login_manager.login_view = "author.login"

