# -*- coding: utf-8 -*-

# Init app and db for global reference

from flask import Flask
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

# Add view controllers here
from app import views as _
from app.tags import views as _
from app.users import views as _
from app.web_components import views as _
