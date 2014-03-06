# -*- coding: utf-8 -*-

from app import app
from app.web_components.models import WebComponent


# Index shows stats for the repository
@app.route("/")
def list_components():
    num_components = len(WebComponent.query.all())
    return "Number of web components: %d" % num_components
