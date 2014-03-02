# -*- coding: utf-8 -*-

from datetime import datetime

from app import db

ROLE_USER = 0
ROLE_ADMIN = 1


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    username = db.Column(db.String(128), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    def __init__(self, username, email, role):
        self.created = datetime.now()
        self.username = username
        self.email = email
        self.role = role

    def __repr__(self):
        return '<User:%s>' % self.username
