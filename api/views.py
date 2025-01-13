from django.shortcuts import render
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, generics

from api.models import Test, Text
from api.permissions import IsOwnerOrReadOnly
from api.serializers import TestSerializer, TextSerializer
from config.exceptions import ClientError, ServerError
from utils.openapi import generate_errors_response


# Create your views here.

class TestAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Test 조회",
        description="Test 조회중 입니다.",
        responses={
            200: TestSerializer(many=True),
            **generate_errors_response([ServerError, ClientError]),
            400: OpenApiResponse(
                description="이름, 설명이 없을떄",
                response={
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "str",
                            "description": "이름 입니다.",
                            "example": "Hong",
                        },
                        "description": {
                            "type": "str",
                            "description": "설명 입니다.",
                            "example": "Hong 입니다.",
                        },
                        "created_dt": {
                            "type": "datetime",
                            "description": "생성 시간",
                            "example": "2025-01-09T08:26:18.332Z",
                        },
                        "updated_dt": {
                            "type": "datetime",
                            "description": "변경 시간",
                            "example": "2025-01-09T08:26:18.332Z",
                        },
                    },
                },
            ),
            **generate_errors_response([ServerError, ClientError]),
        }
    )
    def get(self, request):
        test = Test.objects.all()
        serializer = TestSerializer(test, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Test 생성",
        description="Test 생성중 입니다.",
        parameters=[
            OpenApiParameter(
                name="name",
                description="이름 입니다.",
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name="description",
                description="설명 입니다.",
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
            ),
        ],
        responses={
            201: OpenApiResponse(
                description="이름, 설명이 있을떄",
                response={
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "str",
                            "description": "이름 입니다.",
                            "example": "이름",
                        },
                        "description": {
                            "type": "str",
                            "description": "설명 입니다.",
                            "example": "설명",
                        },
                    },
                }
            ),
            400: OpenApiResponse(
                description="이름, 설명이 없을떄",
                response={
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "str",
                            "description": "이름 입니다.",
                            "example": "이름",
                        },
                        "description": {
                            "type": "str",
                            "description": "설명 입니다.",
                            "example": "설명",
                        },
                    },
                }
            ),
        },
    )
    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer




# class TestListAPIVIew(generics.ListCreateAPIView):
#     queryset = Test.objects.all().order_by("-id")
#     serializer_class = TestSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [SessionAuthentication]
#
#
# class TestDetailAPIVIew(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Test.objects.all().order_by("-id")
#     serializer_class = TestSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [SessionAuthentication]

class TestView(APIView):
    def get(self, request):
        raise ServerError()
