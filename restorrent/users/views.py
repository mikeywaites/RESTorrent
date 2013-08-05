#!/usr/bin/python
#-*- coding: utf-8 -*-

from flask import (Blueprint, request, render_template, flash,
                   g, session, redirect, url_for)
from werkzeug import check_password_hash, generate_password_hash

from restorrent import db
from restorrent.users.decorators import requires_login

mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/me/')
def home():
    return render_template("base.html")
