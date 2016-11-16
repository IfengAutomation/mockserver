from flask import Flask, redirect, url_for

from mockserver.blueprints import api
from mockserver.blueprints import manager
from mockserver.blueprints import mock

app = Flask('Mock')
app.register_blueprint(mock.bp)
app.register_blueprint(api.bp)
app.register_blueprint(manager.bp)


@app.route('/')
def index():
    return redirect(url_for('manager.root'))
