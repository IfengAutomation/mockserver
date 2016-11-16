from flask import Blueprint, render_template
from mockserver.interface_manager import interface_manager


manager = Blueprint('manager', __name__,
                    url_prefix='/mock_manager',
                    template_folder='templates',
                    static_folder='static')


@manager.route('/')
def root():
    return render_template('index.html', interface_list=interface_manager.interface_list)
