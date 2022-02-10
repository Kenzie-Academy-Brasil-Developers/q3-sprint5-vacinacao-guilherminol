

from http import HTTPStatus


def get_all_logs():
    return {'msg': 'GET ALL LOGS'},HTTPStatus.OK

def add_log():
    return {'msg': 'ADD LOG'},HTTPStatus.CREATED