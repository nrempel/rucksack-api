# -*- coding: utf-8 -*-

import os

# Determine config file path based on environment
environment = os.environ['ENVIRONMENT']
config_path = 'config.%s' % environment
