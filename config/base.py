# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'localhost')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db')
