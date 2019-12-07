from sqlalchemy import desc
from sqlalchemy.dialects.postgresql import JSON, UUID

from app.database import BaseMixin, db


class User(BaseMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    n_usp = db.Column(db.Integer(), unique=True, nullable=False)
    polls = db.relationship('Poll', back_populates='user')

    def __init__(self, email, name, n_usp):
        self.email = email
        self.name = name
        self.n_usp = n_usp

class Poll(BaseMixin, db.Model):
    __tablename__ = "polls"

    id = db.Column(db.Integer(), primary_key=True)
    votes = db.Column(db.Integer(), default=0)
    title = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='polls')

    def __init__(self, title, votes):
        self.title = title
        self.votes = votes
