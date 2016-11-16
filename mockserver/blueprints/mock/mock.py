from flask import Blueprint


mock = Blueprint('mock', __name__, url_prefix='/mock')


@mock.route('/')
@mock.route('/<path:path>')
def mock_handler(path=None):
    return 'MOCK'
