# -*- coding: utf-8 -*-

from datetime import datetime

from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

# Many-to-many helper table
components_tags = db.Table(
    'components_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('component_id', db.Integer, db.ForeignKey('component.id'))
)


class User(db.Model):
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


class WebComponent(db.Model):
    __tablename__ = 'components'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    name = db.Column(
        db.String,
        index=True,
        unique=True)
    description = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    owner = db.relationship(
        'User', backref=db.backref('components', lazy='dynamic'))
    repository_url = db.Column(db.String(256))
    tags = db.relationship(
        'Tag',
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


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    name = db.Column(db.String(64), index=True, unique=True)

    def __init__(self, name):
        self.created = datetime.now()
        self.name = name

    def __repr__(self):
        return '<Tag:%s>' % self.name
