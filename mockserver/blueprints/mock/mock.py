from flask import Blueprint, request
from mockserver.interface_manager import interface_manager
from mockserver import recorder


mock = Blueprint('mock', __name__, url_prefix='/mock')


@mock.route('/', methods=['GET', 'POST'])
@mock.route('/<path:path>', methods=['GET', 'POST'])
def mock_handler(path=None):
    recorder.add(request.url)
    interface = interface_manager.find_interface(url=request.url)
    if not interface:
        return 'Interface not found', 404
    return interface.body.decode()
