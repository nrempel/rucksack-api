# -*- coding: utf-8 -*-

from flask.ext.restful import Resource, reqparse

from app import api, db
from app.tags.models import Tag
from app.web_components.models import WebComponent


parser = reqparse.RequestParser()
parser.add_argument('name', type=str)


class TagList(Resource):
    def get(self, id):
        web_component = WebComponent.query.filter_by(id=id).first_or_404()
        return [
            dict(tag)
            for tag
            in web_component.tags.all()]

    def post(self, id):
        args = parser.parse_args()
        web_component = WebComponent.query.filter_by(id=id).first_or_404()

        # Get or create
        name = args['name']
        tag = Tag.query.filter_by(name=name).first()
        if not tag:
            tag = Tag(name=name)

        web_component.tags.append(tag)
        db.session.commit()

        return dict(web_component)


api.add_resource(TagList, '/web_components/<int:id>/tags')
