from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateField, FileField, SelectField, validators
from wtforms.validators import DataRequired
from app.models import Question

class QuestionForm(FlaskForm):
    category = SelectField('Category', [validators.DataRequired()],
    choices=["General Knowledge", "Entertainment: Books", "Entertainment: Film",
    "Entertainment: Music", "Entertainment: Musicals & Theatres", "Entertainment: Television",
    "Entertainment: Video Games", "Entertainment: Japanese Anime & Manga", "Entertainment: Board Games", "Science & Nature",
    "Science: Computers", "Science: Mathematics", "Mythology", "Sports",
    "Geography", "History", "Politics", "Art", "Celebrities", "Animals", "Vehicles",
    "Entertainment: Comics", "Science: Gadgets", "Entertainment: Cartoon & Animations"])
    type = SelectField('Type', [validators.DataRequired()], choices=["multiple", "boolean"])
    difficulty = SelectField('Difficulty', [validators.DataRequired()], choices=["easy", "medium", "hard"])
    question = StringField('Question', [validators.DataRequired()])
    correct_answer = StringField('Correct Answer', [validators.DataRequired()])
    incorrect_answers = StringField('Incorrect Answers', [validators.DataRequired()])
