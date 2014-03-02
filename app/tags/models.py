# -*- coding: utf-8 -*-

from datetime import datetime

from app import db


class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    name = db.Column(db.String(64), index=True, unique=True)

    def __init__(self, name):
        self.created = datetime.now()
        self.name = name

    def __repr__(self):
        return '<Tag:%s>' % self.name
