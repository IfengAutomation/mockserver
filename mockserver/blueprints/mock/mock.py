from flask import Blueprint, request
from mockserver.interface_manager import interface_manager


mock = Blueprint('mock', __name__, url_prefix='/mock')


@mock.route('/')
@mock.route('/<path:path>')
def mock_handler(path=None):
    interface = interface_manager.find_interface(url=request.url)
    if not interface:
        return 'Interface not found', 404
    return interface.body.decode()
