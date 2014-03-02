# -*- coding: utf-8 -*-

from fabric.operations import local


def shell():
    local('PYTHONSTARTUP=shell_env.py python')
