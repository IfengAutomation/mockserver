from flask_script import Manager
import mockserver
from mockserver.database import database
import os


manager = Manager(mockserver.get_app())


@manager.command
def init():
    if os.path.exists(mockserver.db_file):
        os.remove(mockserver.db_file)
    database.db.create_all()


@manager.command
def test_data():
    for i in range(50):
        interface = database.Interface('Demo_'+str(i), 'http://www.ifeng.com')
        database.db.session.add(interface)
    database.db.session.commit()
