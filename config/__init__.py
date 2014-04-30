# -*- coding: utf-8 -*-

import os

# Determine config file path based on environment
environment = os.getenv('ENVIRONMENT', 'local')
config_path = 'config.%s' % environment
