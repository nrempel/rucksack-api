# -*- coding: utf-8 -*-

from datetime import datetime

from app import db
from app.util import unix_time


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    username = db.Column(db.String(128), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)

    def __init__(self, username, email):
        self.created = datetime.now()
        self.username = username
        self.email = email

    def __iter__(self):
        return {
            'id': self.id,
            'created': unix_time(self.created),
            'username': self.username,
            'email': self.email
        }.iteritems()

    def __repr__(self):
        return '<User:%s>' % self.username
