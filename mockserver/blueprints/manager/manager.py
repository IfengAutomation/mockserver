from flask import Blueprint, render_template, request, redirect, url_for
from mockserver import interface_manager
from .forms import InterfaceEditor


manager = Blueprint('manager', __name__,
                    url_prefix='/mock_manager',
                    template_folder='templates',
                    static_folder='static')


@manager.route('/')
def root():
    return render_template('index.html', interface_list=interface_manager.get_interface_list())


@manager.route('/interface_editor', methods=['GET', 'POST'])
@manager.route('/interface_editor/<path:interface_id>', methods=['GET', 'POST'])
def interface_editor(interface_id=None):
    form = InterfaceEditor(request.form)
    if request.method == 'POST' and form.validate():
        if form.id.data:
            # update
            interface_id = form.id.data
            interface = interface_manager.get_interface(interface_id)
            interface = form.update_to_db_instance(interface)
            interface_manager.update_interface(interface)
        else:
            # create new
            interface = form.create_new_instance()
            interface_manager.add_interface(interface)
        return redirect(url_for('manager.root'))
    if interface_id:
        interface = interface_manager.get_interface(interface_id)
        form.update_from_db_instance(interface)
    return render_template('interface_editor.html', form=form)
