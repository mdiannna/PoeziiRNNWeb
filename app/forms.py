from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


class PasteTextForm(FlaskForm):
    text = StringField('text', validators=[DataRequired()])
    submit = SubmitField('Ok')
