import json

from datetime import datetime, date
from decimal import Decimal

from rest_framework import response
from rest_framework import status as status_code
from library.exception import MessageException

class ApiResponse:

    status = False
    data = None
    message = None

    def __init__(self, status=False, data=None, message=None):
        self.status = status
        self.data = data
        self.message = json.dumps(message) if isinstance(message, dict) else str(message)


def json_build(data):
    if isinstance(data, dict):
        for k, v in data.items():
            data[k] = json_build(v)

    if isinstance(data, list):
        for i, v in enumerate(data):
            data[i] = json_build(v)

    if isinstance(data, tuple):
        data = json_build([item for item in data])

    if isinstance(data, datetime):
        data = str(data)

    if isinstance(data, date):
        data = str(data)

    if isinstance(data, int):
        data = str(data)

    if isinstance(data, Decimal):
        data = str(data)

    return data


def build_response(api_response):
    msg_exception = MessageException()
    status = api_response.status
    data = api_response.data
    message = api_response.message

    _status_code = status_code.HTTP_200_OK if status else status_code.HTTP_400_BAD_REQUEST

    if msg_exception.duplicate_error().search(message):
        message = 'Duplicate Entry Value'

    if data:
        data = json_build(data)

    raw_data = {
        "status": status, "data": data, "message": message
    }

    return response.Response(data=raw_data, status=_status_code)
