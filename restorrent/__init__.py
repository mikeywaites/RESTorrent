from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_environments import Environments

app = Flask(__name__)
app.config.from_object('restorrent.config')
env = Environments(app)

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from restorrent.users.views import mod as users
app.register_blueprint(users)
