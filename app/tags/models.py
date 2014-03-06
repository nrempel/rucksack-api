# -*- coding: utf-8 -*-

from datetime import datetime

from app import db
from app.util import unix_time


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    name = db.Column(db.String(64), index=True, unique=True)

    def __init__(self, name):
        self.created = datetime.now()
        self.name = name

    def __iter__(self):
        return {
            'id': self.id,
            'created': unix_time(self.created),
            'name': self.name
        }.iteritems()

    def __repr__(self):
        return '<Tag:%s>' % self.name
