import re
import datetime
import socket

template_pattern = '\{%.*?%\}'
regex = re.compile(template_pattern)


def _now():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def _today():
    return datetime.datetime.now().strftime('%Y-%m-%d')


def _tomorrow():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return tomorrow.strftime('%Y-%m-%d')


def _day_after_tomorrow():
    day_after_tomorrow = datetime.date.today() + datetime.timedelta(days=2)
    return day_after_tomorrow.strftime('%Y-%m-%d')


def _server_host():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip+':8080'

inner_func = {
    'datetime.now': _now,
    'datetime.today': _today,
    'datetime.tomorrow': _tomorrow,
    'datetime.day_after_tomorrow': _day_after_tomorrow,
    'server_host': _server_host
}


def render(json_str):
    all_template_func = regex.findall(json_str)
    for temp_func in all_template_func:
        json_str = _replace(json_str, temp_func)
    return json_str


def _replace(line, temp_func):
    func = inner_func.get(temp_func[2:-2].strip())
    if func:
        res = func()
        return line.replace(temp_func, res)
    else:
        return line.replace(temp_func, '')
