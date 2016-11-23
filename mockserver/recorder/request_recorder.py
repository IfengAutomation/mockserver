_MAX_LEN = 20

request_list = []


def add(url):
    request_list.append(url)
    if len(request_list) > _MAX_LEN:
        request_list.pop(0)


def clear():
    global request_list
    request_list = []


def get():
    return request_list
