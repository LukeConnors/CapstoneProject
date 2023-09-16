from app.models import db, Incorrect_answer, environment, SCHEMA
from sqlalchemy.sql import text

def seed_incorrect_answers():
    ia1 = Incorrect_answer(
        user_id=1,
        question_id=4
    )

    ia2 = Incorrect_answer(
        user_id=1,
        question_id=16
    )

    ia3 = Incorrect_answer(
        user_id=1,
        question_id=45
    )

    ia4 = Incorrect_answer(
        user_id=1,
        question_id=72
    )

    ia5 = Incorrect_answer(
        user_id=1,
        question_id=63
    )

    ia6 = Incorrect_answer(
        user_id=1,
        question_id=56
    )

    ia7 = Incorrect_answer(
        user_id=1,
        question_id=88
    )

    ia8 = Incorrect_answer(
        user_id=1,
        question_id=60
    )

    ia9 = Incorrect_answer(
        user_id=1,
        question_id=20
    )

    ia10 = Incorrect_answer(
        user_id=2,
        question_id=74
    )

    ia11 = Incorrect_answer(
        user_id=2,
        question_id=23
    )

    ia12 = Incorrect_answer(
        user_id=2,
        question_id=27
    )

    ia13 = Incorrect_answer(
        user_id=2,
        question_id=81
    )

    ia14 = Incorrect_answer(
        user_id=2,
        question_id=63
    )

    ia15 = Incorrect_answer(
        user_id=2,
        question_id=84
    )

    ia16 = Incorrect_answer(
        user_id=3,
        question_id=5
    )

    ia17 = Incorrect_answer(
        user_id=3,
        question_id=49
    )

    ia18 = Incorrect_answer(
        user_id=4,
        question_id=77
    )

    ia19 = Incorrect_answer(
        user_id=5,
        question_id=60
    )

    ia20 = Incorrect_answer(
        user_id=5,
        question_id=33
    )

    ia21 = Incorrect_answer(
        user_id=5,
        question_id=27
    )

    ia22 = Incorrect_answer(
        user_id=6,
        question_id=30
    )

    ia23 = Incorrect_answer(
        user_id=6,
        question_id=64
    )

    ia24 = Incorrect_answer(
        user_id=7,
        question_id=78
    )

    ia25 = Incorrect_answer(
        user_id=7,
        question_id=80
    )

    ia26 = Incorrect_answer(
        user_id=8,
        question_id=82
    )

    ia27 = Incorrect_answer(
        user_id=9,
        question_id=45
    )

    ia28 = Incorrect_answer(
        user_id=9,
        question_id=56
    )

    ia29 = Incorrect_answer(
        user_id=9,
        question_id=64
    )

    ia30 = Incorrect_answer(
        user_id=9,
        question_id=71
    )

    ia31 = Incorrect_answer(
        user_id=10,
        question_id=85
    )

    ia32 = Incorrect_answer(
        user_id=10,
        question_id=10
    )

    db.session.add_all([
        ia1, ia2, ia3, ia4, ia5, ia6, ia7, ia8, ia9, ia10,
        ia11, ia12, ia13, ia14, ia15, ia16, ia17, ia18, ia19, ia20,
        ia21, ia22, ia23, ia24, ia25, ia26, ia27, ia28, ia29, ia30,
        ia31, ia32
    ])

    db.session.commit()

def incorrect_answers():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.incorrect_answers RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM incorrect_answers"))

    db.session.commit()
