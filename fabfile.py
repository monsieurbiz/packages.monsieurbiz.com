#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import local, run, cd, env, task, put, abort, get
from distutils.util import strtobool


# Settings
# ¯¯¯¯¯¯¯¯

env.hosts = ["monsieurbiz@monsieurbiz.com"]

@task
def refresh():
    """ Refresh packages """
    with cd('/home/monsieurbiz/web/packages.monsieurbiz.com'):
        _fetch()
        _build()

@task
def deploy():
    """ Deploy and refresh packages """
    with cd('/home/monsieurbiz/web/packages.monsieurbiz.com'):
        _fetch()
        run('composer install -o --no-dev')
        _build()

def _fetch():
    run('git fetch')
    run('git checkout packages')
    run('git reset --hard origin/packages')

def _build():
    run('php bin/satis build satis.json web/')
