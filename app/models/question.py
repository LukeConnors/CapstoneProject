from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func

from .db import db, environment, SCHEMA, add_prefix_for_prod

class Question(db.Model):
    __tablename__='questions'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')),nullable=False)
    category = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    difficulty= db.Column(db.String, nullable=False)
    question= db.Column(db.String, nullable=False)
    correct_answer = db.Column(db.String, nullable=False)
    incorrect_answers = db.Column(db.String, nullable=False)

    # external relation: foreign key
    user = db.relationship('User', back_populates='question')

    # INTERNAL-MODEL RELATIONS (PRIMARY KEY):
    deck_question = db.relationship('Deck_question', back_populates='question')
    correct = db.relationship('Correct_answer', back_populates='question')
    incorrect = db.relationship('Incorrect_answer', back_populates='question')


    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'category': self.category,
            'type': self.type,
            'difficulty': self.difficulty,
            'question': self.question,
            'correct_answer': self.correct_answer,
            'incorrect_answers': self.incorrect_answers
        }
