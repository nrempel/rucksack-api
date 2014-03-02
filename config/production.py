# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

print os.environ['PORT']
print int(os.environ['PORT'])

PORT = int(os.environ['PORT'])
DEBUG = False
CSRF_ENABLED = True
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db')
