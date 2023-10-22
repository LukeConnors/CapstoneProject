from app.models import db, Correct_answer, environment, SCHEMA
from sqlalchemy.sql import text

def seed_correct_answers():
    ca1 = Correct_answer(
        user_id=1,
        question_id=2
    )

    ca2 = Correct_answer(
        user_id=1,
        question_id=4
    )

    ca3 = Correct_answer(
        user_id=1,
        question_id=5
    )

    ca4 = Correct_answer(
        user_id=1,
        question_id=6
    )

    ca5 = Correct_answer(
        user_id=1,
        question_id=7
    )

    ca6 = Correct_answer(
        user_id=1,
        question_id=15
    )

    ca7 = Correct_answer(
        user_id=1,
        question_id=85
    )

    ca8 = Correct_answer(
        user_id=1,
        question_id=57
    )

    ca9 = Correct_answer(
        user_id=1,
        question_id=72
    )

    ca10 = Correct_answer(
        user_id=2,
        question_id=56
    )

    ca11 = Correct_answer(
        user_id=2,
        question_id=22
    )

    ca12 = Correct_answer(
        user_id=2,
        question_id=5
    )

    ca13 = Correct_answer(
        user_id=2,
        question_id=28
    )

    ca14 = Correct_answer(
        user_id=2,
        question_id=63
    )

    ca15 = Correct_answer(
        user_id=2,
        question_id=68
    )

    ca16 = Correct_answer(
        user_id=3,
        question_id=9
    )

    ca17 = Correct_answer(
        user_id=3,
        question_id=82
    )

    ca18 = Correct_answer(
        user_id=4,
        question_id=79
    )

    ca19 = Correct_answer(
        user_id=5,
        question_id=26
    )

    ca20 = Correct_answer(
        user_id=5,
        question_id=80
    )

    ca21 = Correct_answer(
        user_id=5,
        question_id=61
    )

    ca22 = Correct_answer(
        user_id=6,
        question_id=11
    )

    ca23 = Correct_answer(
        user_id=6,
        question_id=66
    )

    ca24 = Correct_answer(
        user_id=7,
        question_id=3
    )

    ca25 = Correct_answer(
        user_id=7,
        question_id=51
    )

    ca26 = Correct_answer(
        user_id=8,
        question_id=13
    )

    ca27 = Correct_answer(
        user_id=9,
        question_id=79
    )

    ca28 = Correct_answer(
        user_id=9,
        question_id=44
    )

    ca29 = Correct_answer(
        user_id=9,
        question_id=59
    )

    ca30 = Correct_answer(
        user_id=9,
        question_id=78
    )

    ca31 = Correct_answer(
        user_id=10,
        question_id=21
    )

    ca32 = Correct_answer(
        user_id=10,
        question_id=59
    )

    db.session.add_all([
        ca1, ca2, ca3, ca4, ca5, ca6, ca7, ca8, ca9, ca10,
        ca11, ca12, ca13, ca14, ca15, ca16, ca17, ca18, ca19, ca20,
        ca21, ca22, ca23, ca24, ca25, ca26, ca27, ca28, ca29, ca30,
        ca31, ca32
    ])

    db.session.commit()

def undo_correct_answers():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.correct_answers RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM correct_answers"))

    db.session.commit()
