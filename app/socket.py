from flask_socketio import SocketIO, emit
import os
from app.models import User, db, Message
from flask_login import current_user

origins ="*"

socketio = SocketIO(cors_allowed_origins=origins)


@socketio.on("message")
def handle_message(data, r_id):
    emit("message", data, broadcast=True)
    current_user_id = current_user.get_id()
    new_message = Message(
        message=data["message"],
        sender_id=current_user_id,
        recipient_id=r_id
    )
    db.session.add(new_message)
    db.session.commit()
