from flask import Blueprint, jsonify, session, request
from flask_login import login_required
from app.models import User, Incorrect_answer, Correct_answer, Question, db

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()

# GET all incorrect answers by userID
@user_routes.route('/<int:id>/incorrect')
def get_incorrect_answers(id):
    incorrect_answers = Incorrect_answer.query.join(Question).filter(Incorrect_answer.user_id == id).all()

    return {"incorrect_answers": [incorrect.to_dict() for incorrect in incorrect_answers ]}


# GET all correct answers by userID
@user_routes.route('/<int:id>/correct')
def get_correct_answers(id):
    correct_answers = Correct_answer.query.join(Question).filter(Correct_answer.user_id == id).all()

    return {"correct_answers": [correct.to_dict() for correct in correct_answers ]}

# # POST an incorrect answer by userID
@user_routes.route('/<int:id>/incorrect', methods=["POST"])
def add_incorrect_answer(id):
    question = request.json

    new_incorrect_answer = Incorrect_answer(
        user_id=id,
        question_id=question["id"]
    )
    db.session.add(new_incorrect_answer)
    db.session.commit()
    return new_incorrect_answer.to_dict()


# # POST a correct answer by userID
@user_routes.route('/<int:id>/correct', methods=["POST"])
def add_correct_answer(id):
    question = request.json

    new_correct_answer = Correct_answer(
        user_id=id,
        question_id=question["id"]
    )
    db.session.add(new_correct_answer)
    db.session.commit()
    return new_correct_answer.to_dict()
