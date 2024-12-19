from rest_framework.exceptions import APIException
from rest_framework.response import Response


class CustomException(APIException):
    name = "CustomException"

    def __init__(self, detail=""):
        self.detail = detail

    def __str__(self):
        return f"{self.name}({self.code}): {self.message}"

    def add_detail(self, detail):
        self.detail = detail

    def response(self):
        return Response(
            {
                "success": False,
                "name": self.name,
                "message": self.message,
                "detail": self.detail,
                "code": self.code,
            }
        )


class ServerError(CustomException):
    name = "ServerError"
    message = "서버 에러입니다."
    code = "S001"


class ClientError(CustomException):
    name = "ClientError"
    message = "클라이언트 에러입니다."
    code = "C001"
