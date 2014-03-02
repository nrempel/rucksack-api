# -*- coding: utf-8 -*-

# from flask import jsonify
from flask.views import MethodView

# from app.users.models import Users
from app.util import register_api


class UsersAPI(MethodView):
    def get(self, id):
        # user = Users.query.filter(id=id)
        return 'Users stub'

    # TODO: implement
    # def put(self, id):
    #     pass

    # def post(self, id):
    #     pass

    # def delete(self, id):
    #     pass

register_api(UsersAPI, 'users', '/users/')
