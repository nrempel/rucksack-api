# -*- coding: utf-8 -*-

from datetime import datetime

from app import db
from app.models import components_tags
from app.users.models import User
from app.tags.models import Tag
from app.util import unix_time


class WebComponent(db.Model):
    __tablename__ = 'web_component'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    name = db.Column(
        db.String,
        index=True,
        unique=True)
    description = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship(
        User, backref=db.backref('web_components', lazy='dynamic'))
    repository_url = db.Column(db.String(256))
    tags = db.relationship(
        Tag,
        secondary=components_tags,
        backref=db.backref('web_components', lazy='dynamic'))

    def __init__(
            self,
            name,
            description,
            owner,
            repository_url):
        self.created = datetime.now()
        self.name = name
        self.description = description
        self.owner = owner
        self.repository_url = repository_url

    def __iter__(self):
        return {
            'id': self.id,
            'created': unix_time(self.created),
            'name': self.name,
            'description': self.description,
            'owner': dict(self.owner),
            'repository_url': self.repository_url,
            'tags': [dict(tag) for tag in self.tags]
        }.iteritems()

    def __repr__(self):
        return '<WebComponent:%s>' % self.name
