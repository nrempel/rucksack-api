# -*- coding: utf-8 -*-

from app import app
from app.models import WebComponent


@app.route("/")
def list_components():
    num_components = len(WebComponent.query.all())
    return "Number of records: %d" % num_components
    # TODO: retrieve, jsonify, and return all records


# @app.route("/", methods=['POST'])
# def insert_component():
#     TODO: create record
