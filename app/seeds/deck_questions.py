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

    dq56 = Deck_question(
        deck_id=9,
        question_id=99
    )

    dq57 = Deck_question(
        deck_id=9,
        question_id=100
    )

    dq58 = Deck_question(
        deck_id=9,
        question_id=101
    )

    dq59 = Deck_question(
        deck_id=9,
        question_id=102
    )

    dq60 = Deck_question(
        deck_id=9,
        question_id=103
    )

    dq61 = Deck_question(
        deck_id=14,
        question_id=104
    )

    dq62 = Deck_question(
        deck_id=14,
        question_id=105
    )

    dq63 = Deck_question(
        deck_id=14,
        question_id=106
    )

    dq64 = Deck_question(
        deck_id=14,
        question_id=107
    )

    dq65 = Deck_question(
        deck_id=14,
        question_id=108
    )

    dq66 = Deck_question(
        deck_id=15,
        question_id=109
    )

    dq67 = Deck_question(
        deck_id=15,
        question_id=110
    )

    dq68 = Deck_question(
        deck_id=15,
        question_id=111
    )

    dq69 = Deck_question(
        deck_id=15,
        question_id=112
    )

    dq70 = Deck_question(
        deck_id=15,
        question_id=113
    )

    dq71 = Deck_question(
        deck_id=16,
        question_id=114
    )

    dq72 = Deck_question(
        deck_id=16,
        question_id=115
    )

    dq73 = Deck_question(
        deck_id=16,
        question_id=116
    )

    dq74 = Deck_question(
        deck_id=16,
        question_id=117
    )

    dq75 = Deck_question(
        deck_id=16,
        question_id=118
    )

    dq76 = Deck_question(
        deck_id=17,
        question_id=119
    )

    dq77 = Deck_question(
        deck_id=17,
        question_id=120
    )

    dq78 = Deck_question(
        deck_id=17,
        question_id=121
    )

    dq79 = Deck_question(
        deck_id=17,
        question_id=122
    )

    dq80 = Deck_question(
        deck_id=17,
        question_id=123
    )

    dq81 = Deck_question(
        deck_id=18,
        question_id=124
    )

    dq82 = Deck_question(
        deck_id=18,
        question_id=125
    )

    dq83 = Deck_question(
        deck_id=18,
        question_id=126
    )

    dq84 = Deck_question(
        deck_id=18,
        question_id=127
    )

    dq85 = Deck_question(
        deck_id=18,
        question_id=128
    )

    dq86 = Deck_question(
        deck_id=19,
        question_id=129
    )

    dq87 = Deck_question(
        deck_id=19,
        question_id=130
    )

    dq88 = Deck_question(
        deck_id=19,
        question_id=131
    )

    dq89 = Deck_question(
        deck_id=19,
        question_id=132
    )

    dq90 = Deck_question(
        deck_id=19,
        question_id=133
    )

    dq91 = Deck_question(
        deck_id=20,
        question_id=134
    )

    dq92 = Deck_question(
        deck_id=20,
        question_id=135
    )

    dq93 = Deck_question(
        deck_id=20,
        question_id=136
    )

    dq94 = Deck_question(
        deck_id=20,
        question_id=137
    )

    dq95 = Deck_question(
        deck_id=20,
        question_id=138
    )

    dq96 = Deck_question(
        deck_id=21,
        question_id=139
    )

    dq97 = Deck_question(
        deck_id=21,
        question_id=140
    )

    dq98 = Deck_question(
        deck_id=21,
        question_id=141
    )

    dq99 = Deck_question(
        deck_id=21,
        question_id=142
    )

    dq100 = Deck_question(
        deck_id=21,
        question_id=143
    )

    dq101 = Deck_question(
        deck_id=22,
        question_id=144
    )

    dq102 = Deck_question(
        deck_id=22,
        question_id=145
    )

    dq103 = Deck_question(
        deck_id=22,
        question_id=146
    )

    dq104 = Deck_question(
        deck_id=22,
        question_id=147
    )

    dq105 = Deck_question(
        deck_id=22,
        question_id=148
    )

    dq106 = Deck_question(
        deck_id=23,
        question_id=149
    )

    dq107 = Deck_question(
        deck_id=23,
        question_id=150
    )

    dq108 = Deck_question(
        deck_id=23,
        question_id=151
    )

    dq109 = Deck_question(
        deck_id=23,
        question_id=152
    )

    dq110 = Deck_question(
        deck_id=23,
        question_id=153
    )

    dq111 = Deck_question(
        deck_id=24,
        question_id=154
    )

    dq112 = Deck_question(
        deck_id=24,
        question_id=155
    )

    dq113 = Deck_question(
        deck_id=24,
        question_id=156
    )

    dq114 = Deck_question(
        deck_id=24,
        question_id=157
    )

    dq115 = Deck_question(
        deck_id=24,
        question_id=158
    )

    dq116 = Deck_question(
        deck_id=25,
        question_id=159
    )

    dq117 = Deck_question(
        deck_id=25,
        question_id=160
    )

    dq118 = Deck_question(
        deck_id=25,
        question_id=161
    )

    dq119 = Deck_question(
        deck_id=25,
        question_id=162
    )

    dq120 = Deck_question(
        deck_id=25,
        question_id=163
    )

    dq121 = Deck_question(
        deck_id=26,
        question_id=164
    )

    dq122 = Deck_question(
        deck_id=26,
        question_id=165
    )

    dq123 = Deck_question(
        deck_id=26,
        question_id=166
    )

    dq124 = Deck_question(
        deck_id=26,
        question_id=167
    )

    dq125 = Deck_question(
        deck_id=26,
        question_id=168
    )

    dq126 = Deck_question(
        deck_id=27,
        question_id=169
    )

    dq127 = Deck_question(
        deck_id=27,
        question_id=170
    )

    dq128 = Deck_question(
        deck_id=27,
        question_id=171
    )

    dq129 = Deck_question(
        deck_id=27,
        question_id=172
    )

    dq130 = Deck_question(
        deck_id=27,
        question_id=173
    )

    dq131 = Deck_question(
        deck_id=28,
        question_id=174
    )

    dq132 = Deck_question(
        deck_id=28,
        question_id=175
    )

    dq133 = Deck_question(
        deck_id=28,
        question_id=176
    )

    dq134 = Deck_question(
        deck_id=28,
        question_id=177
    )

    dq135 = Deck_question(
        deck_id=28,
        question_id=178
    )


    db.session.add_all([
        dq1, dq2, dq3, dq4, dq5, dq6, dq7, dq8, dq9, dq10,
        dq11, dq12, dq13, dq14, dq15, dq16, dq17, dq18, dq19, dq20,
        dq21, dq22, dq23, dq24, dq25, dq26, dq27, dq28, dq29, dq30,
        dq31, dq32, dq33, dq34, dq35, dq36, dq37, dq38, dq39, dq40,
        dq41, dq42, dq43, dq44, dq45, dq46, dq47, dq48, dq49, dq50,
        dq51, dq52, dq53, dq54, dq55, dq56, dq57, dq58, dq59, dq60,
        dq61, dq62, dq63, dq64, dq65, dq66, dq67, dq68, dq69, dq70,
        dq71, dq72, dq73, dq74, dq75, dq76, dq77, dq78, dq79, dq80,
        dq81, dq82, dq83, dq84, dq85, dq86, dq87, dq88, dq89, dq90,
        dq91, dq92, dq93, dq94, dq95, dq96, dq97, dq98, dq99, dq100,
        dq101, dq102, dq103, dq104, dq105, dq106, dq107, dq108, dq109,
        dq110, dq111, dq112, dq113, dq114, dq115, dq116, dq117, dq118,
        dq119, dq120, dq121, dq122, dq123, dq124, dq125, dq126, dq127,
        dq128, dq129, dq130, dq131, dq132, dq133, dq134, dq135

    ])

    db.session.commit()

def undo_deck_questions():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.deck_questions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM deck_questions"))

    db.session.commit()
