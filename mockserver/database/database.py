from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()


class Interface(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    url = db.Column(db.String)
    query_string = db.Column(db.String)
    active = db.Column(db.Boolean, index=True)
    default = db.Column(db.Boolean, index=True)
    body = db.Column(db.Binary)
    mock_prefix = db.Column(db.String)

    def __init__(self, name, url, active=True, default=True, body=None, mock_prefix=None, query_string=None):
        self.name = name
        self.url = url
        self.active = active
        self.default = default
        if body:
            self.body = body
        if mock_prefix:
            self.mock_prefix = mock_prefix
        self.query_string = query_string

    def get_json_body(self):
        return json.dumps(json.loads(self.body.decode()), ensure_ascii=False, indent=4)

    def to_dict(self):
        return {
            'name': self.name,
            'url': self.url,
            'default': self.default,
            'active': self.active,
            'mock_prefix': self.mock_prefix,
            'body': self.body.decode(),
            'query_string': self.query_string
        }

    @classmethod
    def from_dict(cls, interface_dict):
        return cls(interface_dict['name'],
                   interface_dict['url'],
                   default=interface_dict['default'],
                   active=interface_dict['active'],
                   body=interface_dict['body'].encode(),
                   mock_prefix=interface_dict['mock_prefix'],
                   query_string=interface_dict['query_string'])
