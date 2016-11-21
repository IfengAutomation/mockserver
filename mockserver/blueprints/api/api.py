from flask import Blueprint
from mockserver.interface_manager import interface_manager


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def index():
    return 'api'


@api.route('/active/<string:name>/<string:status>')
def active(name, status):
    if status.lower() == 'true':
        status = True
    else:
        status = False
    if interface_manager.change_interface_active(name, status):
        return 'OK'
    else:
        return 'FAIL'


@api.route('/reset')
def reset():
    interface_manager.reset()
    return 'OK'
