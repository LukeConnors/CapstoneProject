from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func

from .db import db, environment, SCHEMA, add_prefix_for_prod

class Deck(db.Model):
    __tablename__='decks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)

    # INTERNAL-MODEL RELATIONS (PRIMARY KEY):
    deck_question = db.relationship('Deck_question', back_populates='deck', cascade="all, delete-orphan")
    review = db.relationship('Review', back_populates='deck', cascade="all, delete-orphan")

    # EXTERNAL-MODEL RELATIONS (FOREIGN KEYS):
    user = db.relationship('User', back_populates='deck')

    def to_dict(self):
        return {
        'id' : self.id,
        'user_id': self.user_id,
        'title': self.title,
        'description': self.description,
        'category': self.category
        }
