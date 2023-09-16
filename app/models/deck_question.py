from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func

from .db import db, environment, SCHEMA, add_prefix_for_prod

class Deck_question(db.Model):
    __tablename__='deck_questions'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deck_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('decks.id')), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('questions.id')), nullable=False)

    # EXTERNAL-MODEL RELATIONS (FOREIGN KEYS):
    deck = db.relationship('Deck', back_populates='deck_question')
    question = db.relationship('Question', back_populates='deck_question')

    def to_dict(self):
        return {
            'id': self.id,
            'deck_id': self.deck_id,
            'question_id': self.question_id
        }
