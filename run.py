#!/usr/bin/python
#-*- coding: utf-8 -*-

from restorrent import app
app.run(host="0.0.0.0", debug=app.config['DEBUG'])
