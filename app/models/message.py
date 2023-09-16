from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func

from .db import db, environment, SCHEMA, add_prefix_for_prod

class Message(db.Model):
    __tablename__='messages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String, nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

    # EXTERNAL-MODEL RELATIONS (FOREIGN KEYS):
    sender_ref = db.relationship('User', foreign_keys='Message.sender_id')
    recipient_ref = db.relationship('User', foreign_keys='Message.recipient_id')


    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message,
            'sender_id': self.sender_id,
            'recipient_id': self.recipient_id
        }
