from flask import Blueprint, request
import requests
from mockserver.database.database import Interface
from urllib.parse import urlparse
from mockserver.interface_manager import interface_manager
import time


proxy = Blueprint('proxy', __name__, url_prefix='/proxy')


@proxy.route('/')
@proxy.route('/<path:path>')
def proxy_handler(path=None):
    index = request.url.find('/proxy')
    real_url = 'http://'+request.url[index+7:]
    parse_res = urlparse(real_url)
    response = requests.get(real_url)

    interface = Interface(parse_res.path, real_url, body=response.text.encode(), mock_prefix=parse_res.hostname)
    if interface.name is '':
        interface.name = 'none_path'

    interface.name += '_'+str(time.time())
    interface_manager.add_interface(interface)
    return response.text, response.status_code


def _get_name(old_name):
    index_line = old_name.rfind('_')
    if index_line == -1:
        return old_name+'_1'
    real_old_name = old_name[:index_line]
    count = old_name[index_line+1:]
    try:
        old_count = int(count)
        return real_old_name+'_'+str(old_count+1)
    except ValueError:
        return old_name+'_1'