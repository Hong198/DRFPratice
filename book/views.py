from django.shortcuts import render, get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse

from rest_framework import viewsets, status, authentication, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book
from book.serializers import BookSerializer
from config.exceptions import ServerError, ClientError
from utils.openapi import generate_errors_response


# Create your views here.
class BookListAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="책 정보",
        description="책 정보 입니다.",
        responses={
            200: BookSerializer(many=True),
            **generate_errors_response([ServerError, ClientError]),
            400: OpenApiResponse(
                description="책 정보 리스트 입니다.",
                response={
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "str",
                            "description": "책 제목",
                            "example": "example"
                        },
                        "content": {
                            "type": "str",
                            "description": "책 내용",
                            "example": "example",
                        },
                        "created_dt": {
                            "type": "datetime",
                            "description": "생성 날짜",
                            "example": "2025-01-13T00:43:18.187Z",
                        },
                        "updated_dt": {
                            "type": "datetime",
                            "description": "업데이트 날짜",
                            "example": "2025-01-13T00:43:18.187Z",
                        }
                    },
                }
            ),
            **generate_errors_response([ServerError, ClientError]),
        },
    )
    def get(self, request):
        book = Book.objects.all().order_by("-id")
        serializer = BookSerializer(book, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="책 생성",
        description="책을 생성합니다. 필수 필드는 'title'과 'content'입니다.",
        request=BookSerializer,
        responses={
            201: OpenApiResponse(BookSerializer, description="책이 성공적으로 생성되었습니다."),
            **generate_errors_response([ServerError, ClientError]),
            400:OpenApiResponse(
                description="책을 생성합니다.",
                response={
                    "type":"object",
                    "properties":{
                        "title": {
                            "type": "str",
                            "description": "책 제목",
                            "example": "example"
                        },
                        "content": {
                            "type": "str",
                            "description": "책 내용",
                            "example": "example",
                        },
                        "created_dt": {
                            "type": "datetime",
                            "description": "생성 날짜",
                            "example": "2025-01-13T00:43:18.187Z",
                        },
                        "updated_dt": {
                            "type": "datetime",
                            "description": "업데이트 날짜",
                            "example": "2025-01-13T00:43:18.187Z",
                        }
                    },
                }
            ),
            **generate_errors_response([ServerError, ClientError]),
        },
    )
    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(APIView):
    def get_object(self, pk):
        book = get_object_or_404(Book, pk=pk)
        return book

    @extend_schema(
        summary="책 상세 정보",
        description="책 상세 정보 입니다.",
        responses={
            200: BookSerializer,
            **generate_errors_response([ServerError, ClientError]),
            400:OpenApiResponse(
                description="책 세부 정보",
                response={
                    "type":"object",
                    "properties":{
                        "title":{
                            "type":"str",
                            "description":"책 제목",
                            "example":"책 제목",
                        },
                        "content":{
                            "type":"str",
                            "description":"책 내용",
                            "example":"책 내용",
                        },
                        "created_dt":{
                            "type":"datetime",
                            "description":"책 세부 생성 날짜",
                            "example":"책 세부 생성 날짜",
                        },
                        "updated_dt":{
                            "type":"datetime",
                            "description":"책 세부 업데이트 날짜",
                            "example":"책 세부 업데이트 날짜",
                        }
                    }
                }
            ),
            **generate_errors_response([ServerError, ClientError]),
        },
    )
    def get(self, request, pk):
        book = self.get_object(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="책 상세 정보 수정",
        description="책 상세 정보 수정 입니다.",
        request=BookSerializer,
        responses={
            200: BookSerializer,
            **generate_errors_response([ServerError, ClientError]),
            400:OpenApiResponse(
                description="책 세부 정보 수정",
                response={
                    "type":"object",
                    "properties":{
                        "title":{
                            "type":"str",
                            "description":"책 상세 정보 수정 제목",
                            "example":"책 제목",
                        },
                        "content":{
                            "type":"str",
                            "description":"책 상세 정보 수정 내용",
                            "example":"책 내용",
                        },
                        "created_dt":{
                            "type":"datetime",
                            "description":"책 상세 정보 수정 생성 날짜",
                            "example":"책 생성 날짜",
                        },
                        "updated_dt":{
                            "type":"datetime",
                            "description":"책 상세 정보 수정 업데이트 날짜",
                            "example":"책 업데이트 날짜",
                        },
                    },
                },
            )
        },
    )
    def patch(self, request, pk):
        book = self.get_object(pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="책 상세 정보 삭제",
        description="책 상세 정보 삭제 입니다.",
        responses={
            204: OpenApiResponse(dict, description="삭제된 정보입니다."),
            404: OpenApiResponse(dict, description="이미 삭제된 정보입니다.")
        },
    )
    def delete(self, request, pk):
        book = self.get_object(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated]


# def
class ExampleView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': '인증 성공!'
        }
        return Response(content)
