from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, length


class LoginForm(FlaskForm):
    username = StringField(
        "Username", render_kw={'placeholder': "Username"})
    password = PasswordField("Password", render_kw={
                             'placeholder': "passwore"})
    remember = BooleanField("Remember me")
    submit = SubmitField("登录")
