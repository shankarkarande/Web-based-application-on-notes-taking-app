from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

# from datetime import datetime


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ntitle = db.Column(db.String(200), nullable=False)
    data = db.Column(db.String(10000), nullable=False)
    date =db.Column(db.DateTime , default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f"{self.ntitle} - {self.note}"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
