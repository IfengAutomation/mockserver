

class Interface:

    def __init__(self, id, name, default, active, url, request_filter=None, body=None):
        self.id = id
        self.name = name
        self.default = default
        self.active = active
        self.url = url
        self.filter = request_filter
        self.body = body


class RequestFilter:
    pass


class InterfaceManager:

    @property
    def interface_list(self):
        return [Interface(i, 'InterfaceDemo', True, True, 'http://www.ifeng.com') for i in range(10)]
