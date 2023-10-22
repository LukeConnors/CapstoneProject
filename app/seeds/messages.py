from app.models import db, Message, environment, SCHEMA


def seed_messages():
    message1 = Message(
        message="Hi my name is demo! I really like your reviews!",
        sender_id=1,
        recipient_id=2
    )

    message2 = Message(
        message="Hi demo! Thanks, I work really hard on them. How are you enjoying Trivia Titan?",
        sender_id=2,
        recipient_id=1
    )

    message3 = Message(
        message="I really like it, I definitely think there is a lot of room for me to grow as someone who loves trivia.",
        sender_id=1,
        recipient_id=2
    )

    message4 = Message(
        message="Hey what did you think of Mythology Deck 1?",
        sender_id=3,
        recipient_id=4
    )

    message5 = Message(
        message="I think it needs way more questions. Definitely a work in progress.",
        sender_id=4,
        recipient_id=3
    )

    db.session.add_all([message1, message2, message3, message4, message5])
    db.session.commit()

def undo_messages():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.messages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM messages"))

    db.session.commit()
