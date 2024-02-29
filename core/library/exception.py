import re

class ResponseException(Exception):

    def __init__(self, message='internal server error', status=500):
        super(ResponseException, self).__init__(message)
        self.message = message
        self.status = status

class BadRequestResponseException(ResponseException):

    def __init__(self, message='bad request'):
        super(BadRequestResponseException, self).__init__(message, status=400)

class MessageException:
    TOO_MANY_REQUEST = [
        "Too Many Requests", "Too Many Redirects"
    ]
    CONNECTION_TIMEOUT = [
        "ReadTimeout", "Read Timed out", "ConnectTimeout", "Connection Timed out", "Connect Timeout", "Timed Out", "Cannot connect to proxy"
    ]
    CONNECTION_ERROR = [
        "Failed to establish a new connection", "Connection reset by peer"
    ]
    PROXY_ERROR = [
        "Cannot connect to proxy"
    ]
    JSON_DECODE_ERROR = [
        "JSONDecodeError"
    ]
    Duplicate = [
        'Cannot insert duplicate key'
    ]

    def too_many_requests(self):
        pattern = r"|".join(self.TOO_MANY_REQUEST)
        return re.compile(pattern=pattern, flags=re.I)

    def connection_timeout(self):
        pattern = r"|".join(self.CONNECTION_TIMEOUT)
        return re.compile(pattern=pattern, flags=re.I)

    def connection_error(self):
        pattern = r"|".join(self.CONNECTION_ERROR)
        return re.compile(pattern=pattern, flags=re.I)

    def proxy_error(self):
        pattern = r"|".join(self.PROXY_ERROR)
        return re.compile(pattern=pattern, flags=re.I)

    def json_decode_error(self):
        pattern = r"|".join(self.JSON_DECODE_ERROR)
        return re.compile(pattern=pattern, flags=re.I)

    def duplicate_error(self):
        pattern = r"|".join(self.Duplicate)
        return re.compile(pattern=pattern, flags=re.I)