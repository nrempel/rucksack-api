# -*- coding: utf-8 -*-

from datetime import datetime

from app import db
from app.models import components_tags
from app.users.models import Users
from app.tags.models import Tags


class WebComponents(db.Model):
    __tablename__ = 'components'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    name = db.Column(
        db.String,
        index=True,
        unique=True)
    description = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    owner = db.relationship(
        Users, backref=db.backref('components', lazy='dynamic'))
    repository_url = db.Column(db.String(256))
    tags = db.relationship(
        Tags,
        secondary=components_tags,
        backref=db.backref('components', lazy='dynamic'))

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

    def __repr__(self):
        return '<WebComponent:%s>' % self.name
