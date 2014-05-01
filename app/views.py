# -*- coding: utf-8 -*-

from app import app


INDEX = """
<a href='/users'>users</a><br>
<a href='/web_components'>web_components</a><br>
"""


# Index shows stats for the repository
@app.route("/")
def index():
    return INDEX
