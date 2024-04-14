from http import HTTPStatus

from exceptions import APIException, ErrorMessages


class BadRequestException(APIException):
    message = ErrorMessages.bad_request
    http_status = HTTPStatus.BAD_REQUEST

    def __init__(self, message=ErrorMessages.bad_request, extra=None):
        super().__init__(
            http_status=HTTPStatus.BAD_REQUEST, message=message, extra=extra
        )

    def __str__(self):
        return "Bad Request errors"
