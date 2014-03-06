# -*- coding: utf-8 -*-

# Helper tables for many-to-many relationships

from app import db

components_tags = db.Table(
    'components_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('component_id', db.Integer, db.ForeignKey('web_component.id'))
)
