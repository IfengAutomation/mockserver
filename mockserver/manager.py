from flask_script import Manager
import mockserver
from mockserver.database import database
import json
import codecs
import os


manager = Manager(mockserver.get_app())


@manager.command
def init():
    if os.path.exists(mockserver.db_file):
        os.remove(mockserver.db_file)
    database.db.create_all()


@manager.command
def dump(bak_file, id=None):
    print('Dump %s start' % bak_file)
    all_data = []
    if id:
        if id.find(',') == -1:
            interface = database.Interface.query.filter_by(id=id).first()
            if interface:
                all_data.append(interface.to_dict())
            else:
                print('Not found any data to dump.')
                return
        else:
            all_ids = id.split(',')
            for _id in all_ids:
                interface = database.Interface.query.filter_by(id=_id).first()
                if interface:
                    all_data.append(interface.to_dict())
    else:
        all_interfaces = database.Interface.query.all()
        if len(all_interfaces) == 0:
            print('Not found any data to dump.')
            return

        for interface in all_interfaces:
            all_data.append(interface.to_dict())
    f = codecs.open(bak_file, 'w', 'utf-8')
    f.write(json.dumps(all_data, ensure_ascii=False, indent=4))
    f.close()
    print('Dump completed')


@manager.command
def load(bak_file):
    print('Load %s start' % bak_file)
    f = codecs.open(bak_file, 'r', 'utf-8')
    all_data = json.loads(f.read())
    f.close()
    for data in all_data:
        interface = database.Interface.from_dict(data)
        if len(database.Interface.query.filter_by(name=interface.name).all()) > 0:
            interface.name = '[Dup.]' + interface.name
        database.db.session.add(interface)
    database.db.session.commit()
    print('Load completed')
