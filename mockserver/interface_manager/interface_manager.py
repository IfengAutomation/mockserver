from mockserver.database.database import Interface
from mockserver.database.database import db


class RequestFilter:
    def __init__(self):
        self.host = None
        self.path = None
        self.args = None

    def execute(self, record):
        return self._host_compare(record) and self._path_compare(record) and self._args_compare(record)

    def _host_compare(self, record):
        if self.host:
            return record.host == self.host
        else:
            return True

    def _path_compare(self, record):
        if self.path:
            return record.path == self.path
        else:
            return True

    def _args_compare(self, record):
        if self.args:
            for arg_name in self.args:
                expect_value = self.args[arg_name]
                if arg_name in record.args:
                    if record.args[arg_name] != expect_value:
                        return False
                else:
                    return False
            return True
        else:
            return True


def get_interface_list():
    return Interface.query.all()


def get_interface(interface_id):
    return Interface.query.filter_by(id=interface_id).first()


def update_interface(interface):
    db.session.commit()


def add_interface(interface):
    db.session.add(interface)
    db.session.commit()
