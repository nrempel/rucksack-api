# -*- coding: utf-8 -*-

import os

from config.base import *

HOST = '0.0.0.0'
PORT = int(os.environ['PORT'])
DEBUG = False
CSRF_ENABLED = True
