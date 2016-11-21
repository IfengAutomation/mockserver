from mockserver.database.database import Interface
from mockserver.database.database import db
from urllib.parse import parse_qs, urlparse


def get_interface_list():
    return Interface.query.all()


def get_interface(interface_id):
    return Interface.query.filter_by(id=interface_id).first()


def update_interface(interface):
    db.session.commit()


def add_interface(interface):
    db.session.add(interface)
    db.session.commit()


def change_interface_active(name, status):
    interface = Interface.query.filter_by(name=name).first()
    if not interface:
        return False
    if interface.active is not status:
        interface.active = not interface.active
        db.session.commit()
    return True


def reset():
    all_record = Interface.query.all()
    for interface in all_record:
        interface.active = interface.default
    db.session.commit()


def _is_args_match(expect, actual):
    for expect_key in expect:
        if expect_key not in actual:
            return False
        else:
            if expect[expect_key] != actual[expect_key]:
                return False
    return True


def find_interface(name=None, url=None):
    if name:
        return _find_interface_by_name(name)
    if url:
        return _find_interface_by_url(url)


def _find_interface_by_name(name):
    return Interface.query.filter_by(name=name).first()


def _find_interface_by_url(url):
    res = urlparse(url)
    args = parse_qs(res.query)
    all_interfaces = Interface.query.filter_by(active=True).all()
    for interface in all_interfaces:
        filter_res = urlparse(interface.url)
        filter_path = '/mock'+interface.mock_prefix+filter_res.path
        if res.path == filter_path:
            if _is_args_match(parse_qs(interface.query_string), args):
                return interface
