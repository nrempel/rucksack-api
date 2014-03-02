# -*- coding: utf-8 -*-

# This file is read when the python interactive shell starts up.
# It's used to run python in the context of the Flask project.

from app import app
from config import config_path

# Config
app.config.from_object(config_path)
