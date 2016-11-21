from flask_sqlalchemy import SQLAlchemy

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


