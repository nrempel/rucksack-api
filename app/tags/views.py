# -*- coding: utf-8 -*-

# from flask import jsonify
from flask.views import MethodView

# from app.tags.models import Tags
from app.util import register_api


class TagsAPI(MethodView):
    def get(self, id):
        # tag = Tags.query.filter(id=id)
        return 'Tags stub'

    # TODO: implement
    # def put(self, id):
    #     pass

    # def post(self, id):
    #     pass

    # def delete(self, id):
    #     pass

register_api(TagsAPI, 'tags', '/tags/')
