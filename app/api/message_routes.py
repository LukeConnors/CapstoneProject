from flask import Blueprint, jsonify, session, request
from app.models import Question, User, Deck, Deck_question, Message, Review, db
from app.forms import DeckForm, ReviewForm
from flask_login import current_user, login_required
from sqlalchemy.orm import joinedload


message_routes = Blueprint('messages', __name__)

# GET all messages
@message_routes.route('/')
def messages():
    messages = Message.query.all()

    return {"messages": [message.to_dict() for message in messages]}

# GET all messages by recipient ID
@message_routes.route('/<int:id>')
def get_messages(id):
        user_id = current_user.id
        messages = Message.query.filter(
            ((Message.recipient_id == id) & (Message.sender_id == user_id)) |
            ((Message.recipient_id == user_id) & (Message.sender_id == id))
        ).all()

        return {"messages": [message.to_dict() for message in messages]}
