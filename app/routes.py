# -*- coding: utf-8 -*-

from app import app
from app.models import WebComponent


@app.route("/")
def hello():
    num_components = WebComponent.query.all().count()
    return "Number of records: %d" % num_components
