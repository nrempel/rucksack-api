# -*- coding: utf-8 -*-

from app import app
from config import config_path

# Config
app.config.from_object(config_path)
# Run
app.run(
    host='0.0.0.0',
    debug=app.config['DEBUG'],
    port=app.config['PORT'])
