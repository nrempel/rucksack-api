# -*- coding: utf-8 -*-

from flask.ext.restful import abort, reqparse, Resource
from sqlalchemy.exc import IntegrityError

from app import api, db
from app.users.models import User

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('email', type=str, required=True)


class UserList(Resource):
    def get(self):
        return [dict(user) for user in User.query.all()]

    def post(self):
        args = parser.parse_args()

        # TODO: Validate email

        username = args['username']
        email = args['email']

        # Validate unique username
        user = User.query.filter_by(username=username).first()
        if user:
            abort(
                409,
                message='Conflict: a user with the username %s already exists'
                % username)

        # Validate unique email
        user = User.query.filter_by(email=email).first()
        if user:
            abort(
                409,
                message='Conflict: a user with the email %s already exists'
                % email)

        # Create new user
        user = User(
            username=args['username'],
            email=args['email'])

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(500)

        return dict(user)

api.add_resource(UserList, '/users')
