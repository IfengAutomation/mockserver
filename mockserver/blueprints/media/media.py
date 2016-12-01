from flask import Blueprint, request
from mockserver import recorder

media = Blueprint('media', __name__,
                  url_prefix='/media',
                  static_folder='static')


@media.before_request
def before_request():
    recorder.add(request.url)
