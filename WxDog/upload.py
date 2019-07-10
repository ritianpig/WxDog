from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_wtf import FlaskForm
from wtforms import SubmitField


class UploadForm(FlaskForm):
    photo = FileField("UploadImg", validators=[
                      FileRequired(), FileAllowed(upload_set=[".jpg", ".png"], message=None)])
    submit = SubmitField()
