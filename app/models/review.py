from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func

from .db import db, environment, SCHEMA, add_prefix_for_prod

class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    deck_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('decks.id')), nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)

    # EXTERNAL-MODEL RELATIONS (FOREIGN KEYS):
    user = db.relationship('User', back_populates='review')
    deck = db.relationship('Deck', back_populates='review')

    def to_dict(self):
        return {
        'id': self.id,
        'user_id': self.user_id,
        'deck_id': self.deck_id,
        'stars': self.stars,
        'description': self.description,
        'user': self.user.to_dict()
        }
