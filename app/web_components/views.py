# -*- coding: utf-8 -*-

# from flask import jsonify
from flask.views import MethodView

from app.util import register_api
# from app.web_components.models import WebComponents


class WebComponentsAPI(MethodView):
    def get(self, id):
        # component = WebComponents.query.filter(id=id)
        return 'WebComponents stub'

    # TODO: implement
    # def put(self, id):
    #     pass

    # def post(self, id):
    #     pass

    # def delete(self, id):
    #     pass

register_api(WebComponentsAPI, 'web_components', '/web_components/')
