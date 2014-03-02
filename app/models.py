# -*- coding: utf-8 -*-

# Helper tables for many-to-many relationships

from app import db

components_tags = db.Table(
    'components_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
    db.Column('component_id', db.Integer, db.ForeignKey('components.id'))
)
