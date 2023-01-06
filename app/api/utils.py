import re
from datetime import datetime


def valid_data(data: dict) -> dict:
    new_data = dict()
    for key, value in data.items():
        new_data[key] = value[0]
        if not _valid_items(key, value[0]):
            continue
        if key == "date":
            try:
                new_data[key] = datetime.strptime(value[0], '%Y-%m-%d')
            except ValueError as e:
                new_data[key] = datetime.strptime(value[0], '%d.%m.%Y')
        if key == "phone":
            new_data[key] = f'+{value[0].strip()}'

    new_data.setdefault('phone', 'str')
    new_data.setdefault('email', 'str')
    new_data.setdefault('date', 'datetime')
    return new_data


def _valid_items(key: str, val: str) -> bool:
    reg = {'email': r'^\S+@\w+.\w{2,4}$',
           'date': r'(\d{4}-\d{2}-\d{2})|(\d{2}.\d{2}.\d{4})',
           'phone': r'^\s7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$',
           }
    if re.fullmatch(reg[key], val):
        return True

    return False


def type_data(data: dict) -> dict:
    new_data = {}
    for key, val in data.items():
        new_data[key] = type(val[0]).__name__
        if key == "date":
            new_data[key] = 'datetime'
    return new_data
