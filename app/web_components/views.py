# -*- coding: utf-8 -*-

from flask.ext.restful import abort, reqparse, Resource

from app import api, db
from app.users.models import User
from app.web_components.models import WebComponent


# Required arguments in API call
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('description', type=str, required=True)
parser.add_argument('owner', type=str, required=True)
parser.add_argument('repository_url', type=str, required=True)


class WebComponentList(Resource):
    def get(self):
        return [
            dict(web_component) for web_component in WebComponent.query.all()]

    def post(self):
        args = parser.parse_args()

        name = args['name']

        # TODO: Validate url?

        # Validate unique name
        web_component = WebComponent.query.filter_by(name=name).first()
        if web_component:
            abort(
                409,
                message='Conflict: ' +
                'a web component with the name %s already exists'
                % name)

        username = args['owner']
        owner = User.query.filter_by(username=username).first()
        if not owner:
            abort(
                400,
                message='Bad Request: username %s doesn\'t exist'
                % username)

        web_component = WebComponent(
            name=args['name'],
            description=args['description'],
            owner=owner,
            repository_url=args['repository_url'])
        db.session.add(web_component)
        db.session.commit()

        return dict(web_component)

api.add_resource(WebComponentList, '/web_components')
