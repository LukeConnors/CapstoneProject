from app.models import db, Deck_question, environment, SCHEMA
from sqlalchemy.sql import text

def seed_deck_questions():
    dq1 = Deck_question(
        deck_id=1,
        question_id=1
    )

    dq2 = Deck_question(
        deck_id=1,
        question_id=2
    )

    dq3 = Deck_question(
        deck_id=1,
        question_id=3
    )


    dq4 = Deck_question(
        deck_id=1,
        question_id=4
    )

    dq5 = Deck_question(
        deck_id=1,
        question_id=5
    )

    dq6 = Deck_question(
        deck_id=1,
        question_id=6
    )

    dq7 = Deck_question(
        deck_id=1,
        question_id=7
    )

    dq8 = Deck_question(
        deck_id=1,
        question_id=8
    )

    dq9 = Deck_question(
        deck_id=1,
        question_id=9
    )

    dq10 = Deck_question(
        deck_id=1,
        question_id=10
    )

    dq11 = Deck_question(
        deck_id=2,
        question_id=40
    )

    dq12 = Deck_question(
        deck_id=2,
        question_id=53
    )

    dq13 = Deck_question(
        deck_id=2,
        question_id=67
    )

    dq14 = Deck_question(
        deck_id=2,
        question_id=74
    )

    dq15 = Deck_question(
        deck_id=2,
        question_id=76
    )

    dq16 = Deck_question(
        deck_id=2,
        question_id=82
    )

    dq17 = Deck_question(
        deck_id=2,
        question_id=84
    )

    dq18 = Deck_question(
        deck_id=2,
        question_id=88
    )

    dq19 = Deck_question(
        deck_id=3,
        question_id=41
    )

    dq20 = Deck_question(
        deck_id=3,
        question_id=44
    )

    dq21 = Deck_question(
        deck_id=3,
        question_id=45
    )

    dq22 = Deck_question(
        deck_id=3,
        question_id=46
    )

    dq23 = Deck_question(
        deck_id=3,
        question_id=47
    )

    dq24 = Deck_question(
        deck_id=3,
        question_id=48
    )

    dq25 = Deck_question(
        deck_id=3,
        question_id=49
    )

    dq26 = Deck_question(
        deck_id=3,
        question_id=50
    )

    dq27 = Deck_question(
        deck_id=3,
        question_id=52
    )

    dq28 = Deck_question(
        deck_id=3,
        question_id=54
    )

    dq29 = Deck_question(
        deck_id=3,
        question_id=55
    )

    dq30 = Deck_question(
        deck_id=3,
        question_id=58
    )

    dq31 = Deck_question(
        deck_id=3,
        question_id=59
    )

    dq32 = Deck_question(
        deck_id=3,
        question_id=60
    )

    dq33 = Deck_question(
        deck_id=3,
        question_id=61
    )

    dq34 = Deck_question(
        deck_id=3,
        question_id=63
    )

    dq35 = Deck_question(
        deck_id=3,
        question_id=66
    )

    dq36 = Deck_question(
        deck_id=3,
        question_id=68
    )

    dq37 = Deck_question(
        deck_id=3,
        question_id=70
    )

    dq38 = Deck_question(
        deck_id=3,
        question_id=71
    )

    dq39 = Deck_question(
        deck_id=3,
        question_id=72
    )


    dq40 = Deck_question(
        deck_id=3,
        question_id=78
    )

    dq41 = Deck_question(
        deck_id=3,
        question_id=72
    )

    dq42 = Deck_question(
        deck_id=3,
        question_id=78
    )

    dq43 = Deck_question(
        deck_id=3,
        question_id=79
    )

    dq44 = Deck_question(
        deck_id=3,
        question_id=81
    )

    dq45 = Deck_question(
        deck_id=4,
        question_id=43
    )

    dq46 = Deck_question(
        deck_id=4,
        question_id=57
    )


    dq47 = Deck_question(
        deck_id=4,
        question_id=69
    )

    dq48 = Deck_question(
        deck_id=4,
        question_id=80
    )

    dq49 = Deck_question(
        deck_id=5,
        question_id=73
    )

    dq50 = Deck_question(
        deck_id=6,
        question_id=64
    )

    dq51 = Deck_question(
        deck_id=6,
        question_id=64
    )

    dq52 = Deck_question(
        deck_id=7,
        question_id=51
    )

    dq53 = Deck_question(
        deck_id=7,
        question_id=56
    )

    dq54 = Deck_question(
        deck_id=7,
        question_id=62
    )

    dq55 = Deck_question(
        deck_id=8,
        question_id=42
    )

    db.session.add_all([
        dq1, dq2, dq3, dq4, dq5, dq6, dq7, dq8, dq9, dq10,
        dq11, dq12, dq13, dq14, dq15, dq16, dq17, dq18, dq19, dq20,
        dq21, dq22, dq23, dq24, dq25, dq26, dq27, dq28, dq29, dq30,
        dq31, dq32, dq33, dq34, dq35, dq36, dq37, dq38, dq39, dq40,
        dq41, dq42, dq43, dq44, dq45, dq46, dq47, dq48, dq49, dq50,
        dq51, dq52, dq53, dq54, dq55
    ])

    db.session.commit()

def undo_deck_questions():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.deck_questions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM deck_questions"))

    db.session.commit()
