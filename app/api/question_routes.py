from flask import Blueprint, jsonify, session, request
from app.models import Question, db
from app.forms import QuestionForm
from flask_login import current_user, login_required

question_routes = Blueprint('questions', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


# GET all questions
@question_routes.route('/')
def questions():
    questions = Question.query.all()

    return {"questions": [question.to_dict() for question in questions]}


# GET a question by ID
@question_routes.route('/<int:id>')
def question_details(id):
    question = Question.query.get(id)
    return question.to_dict()

# POST a question
@question_routes.route("/", methods=["POST"])
def create_question():
    form = QuestionForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        new_question = Question(
            category=form.data["category"],
            type=form.data["type"],
            difficulty=form.data["difficulty"],
            question=form.data["question"],
            correct_answer=form.data["correct_answer"],
            incorrect_answers=form.data["incorrect_answers"]
        )
        db.session.add(new_question)
        db.session.commit()
        return new_question.to_dict()

# PUT a question by ID
@question_routes.route("/<int:id>", methods=["PUT"])
def edit_question(id):
    form = QuestionForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        question = Question.query.get(id)
        if question:
            if form.data.get("category"):
                question.category = form.data["category"]
            if form.data.get("type"):
                question.type = form.data["type"]
            if form.data.get("difficulty"):
                question.difficulty = form.data["difficulty"]
            if form.data.get("question"):
                question.question = form.data["question"]
            if form.data.get("correct_answer"):
                question.correct_answer = form.data["correct_answer"]
            if form.data.get("incorrect_answers"):
                question.incorrect_answers = form.data["incorrect_answers"]

            db.session.commit()
            return question.to_dict()
        else:
            return jsonify({"error": "Question not found"}), 404
    else:
        return jsonify({"error": "Invalid form data", "form_errors": form.errors}), 400


# DELETE a question by ID
# @question_routes.route("/<int:id>", methods=["DELETE"])
# def delete_question(id):
#     question = Question.question.get(id)

#     if not question:
#         return jsonify({"error": "Question not found"})

#     if Question
