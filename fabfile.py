# -*- coding: utf-8 -*-

from fabric.operations import local

ENVIRONMENT_LOCAL = 'local'
ENVIRONMENT_PRODUCTION = 'production'

# Run an interactive shell in context of this Flask project
def shell(environment=ENVIRONMENT_LOCAL):
  if environment == ENVIRONMENT_LOCAL:
    local('PYTHONSTARTUP=shell_env.py python')
  elif environment == ENVIRONMENT_PRODUCTION:
    local('heroku run PYTHONSTARTUP=shell_env.py python')
  else:
    print 'Invalid argument'

# Run the server locally
def run():
  local('python run.py')

# Deploy to heroku
def deploy():
  local('git push heroku master:master')
