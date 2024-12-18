from drf_spectacular.utils import inline_serializer
from rest_framework import serializers


def generate_errors_response(errors):
    result = {}
    for err in errors:
        data = inline_serializer(
            name=err.name,
            fields={
                "success": serializers.BooleanField(default=False),
                "code": serializers.CharField(default=err.code),
                "message": serializers.CharField(default=err.message),
                "detail": serializers.CharField(default=""),
            },
        )
        result.update({err.code: data})
    return result
