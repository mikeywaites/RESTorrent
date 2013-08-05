#!/usr/bin/python
#-*- coding: utf-8 -*-

import os

class Config(object):

    DEBUG = False
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    ADMINS = frozenset(['mikey.waites@gmail.com'])
    SECRET_KEY = '640d829610b7436fb0f84d9843862d78'
    THREADS_PER_PAGE = 8
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "049f9ef6011841e7816673c83a592fdc"


class Development(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://scott:tiger@localhost/mydatabase'
