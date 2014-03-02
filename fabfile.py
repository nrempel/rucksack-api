# -*- coding: utf-8 -*-

from fabric.operations import local


# Run an interactive shell in context of this Flask project
def shell():
    local('PYTHONSTARTUP=shell_env.py python')
