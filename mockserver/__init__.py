from flask import Flask, redirect, url_for
import os

from mockserver.blueprints import api
from mockserver.blueprints import manager
from mockserver.blueprints import mock
from mockserver.blueprints import proxy
from mockserver.database import database
from mockserver.blueprints import media

package_root = os.path.abspath(os.path.join(__file__, os.pardir))
root = os.path.abspath(os.path.join(package_root, os.pardir))
db_file = os.path.join(root, 'interface.db')

app = Flask('Mock')
app.register_blueprint(mock.bp)
app.register_blueprint(api.bp)
app.register_blueprint(manager.bp)
app.register_blueprint(proxy.bp)
app.register_blueprint(media.bp)


@app.route('/')
def index():
    return redirect(url_for('manager.root'))


def init():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_file
    database.db.init_app(app)


def get_app():
    init()
    return app
