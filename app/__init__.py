# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

environment = os.environ['ENVIRONMENT']

app = Flask(__name__)
app.config.from_object('settings.%s' % environment)
db = SQLAlchemy(app)

from app import routes, models
