# -*- coding: utf-8 -*-

from app import app
from config import config_path

# Config
app.config.from_object(config_path)
# Run
app.run(debug=app.config['DEBUG'])
