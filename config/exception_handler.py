import traceback

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler
from .exceptions import *


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None or isinstance(exc, ServerError):
        detail = "\n" + traceback.format_exc()
        # detail = exc.detail
        error = ServerError()
        error.add_detail(detail=detail)
        return error.response()

    return response
