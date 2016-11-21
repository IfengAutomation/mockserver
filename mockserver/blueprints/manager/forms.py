from wtforms import Form, StringField, TextAreaField, HiddenField, BooleanField
from mockserver.database.database import Interface


class InterfaceEditor(Form):

    id = HiddenField('ID')
    name = StringField('Name')
    url = StringField('URL')
    mock_prefix = StringField('Mock Prefix')
    default = BooleanField('Default')
    active = BooleanField('Active')
    body = TextAreaField('Response Body')
    query_string = StringField('QueryString')

    def update_from_db_instance(self, interface):
        self.id.data = interface.id
        self.name.data = interface.name
        self.url.data = interface.url
        self.mock_prefix.data = interface.mock_prefix
        self.default.data = interface.default
        self.active.data = interface.active
        self.body.data = interface.body.decode()
        self.query_string.data = interface.query_string

    def update_to_db_instance(self, interface):
        interface.id = self.id.data
        interface.name = self.name.data
        interface.url = self.url.data
        interface.active = self.active.data
        interface.default = self.default.data
        interface.mock_prefix = self.mock_prefix.data
        interface.body = self.body.data.encode()
        interface.query_string = self.query_string.data
        return interface

    def create_new_instance(self):
        return Interface(self.name.data,
                         self.url.data,
                         self.active.data,
                         self.default.data,
                         self.body.data.encode(),
                         self.mock_prefix.data,
                         self.query_string.data)

