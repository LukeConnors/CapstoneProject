from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateField, FileField, SelectField, validators
from wtforms.validators import DataRequired
from app.models import Review


class ReviewForm(FlaskForm):
    stars = IntegerField('Stars', [validators.DataRequired()])
    description = StringField('Description', [validators.DataRequired()])
