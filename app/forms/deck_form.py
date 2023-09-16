from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateField, FileField, SelectField, validators
from wtforms.validators import DataRequired
from app.models import Deck


class DeckForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    description = StringField('Description', [validators.DataRequired()])
    category = SelectField('Category', [validators.DataRequired()],
    choices=["General Knowledge", "Science", "Entertainment",
    "Science & Nature", "Mythology", "Geography", "History", "Celebrities"])
