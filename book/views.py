from django.shortcuts import render, get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse

from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book
from book.serializers import BookSerializer


# Create your views here.
class BookListAPIView(APIView):
    @extend_schema(
        summary="책 정보",
        description="책 정보 입니다.",
        responses={
            200: BookSerializer(many=True),
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

    #
    # @extend_schema(
    #     summary="Retrieve a list of books",
    #     description="Returns a paginated list of all books in the database.",
    #     tags=["Books"],  # Swagger 태그 추가
    # )
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    #
    # @extend_schema(
    #     summary="Retrieve a single book",
    #     description="Fetch a book by its ID.",
    #     tags=["Books"],
    # )
    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)
    #
    # @extend_schema(
    #     summary="Create a new book",
    #     description="Create a new book record by providing the required data.",
    #     tags=["Books"],
    #     request=BookSerializer,  # 요청에 사용되는 Serializer 명시
    #     responses={201: BookSerializer},  # 응답에 사용되는 Serializer 명시
    # )
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)
    #
    # @extend_schema(
    #     summary="Update a book",
    #     description="Update an existing book by providing its ID and new data.",
    #     tags=["Books"],
    # )
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)
    #
    # @extend_schema(
    #     summary="Delete a book",
    #     description="Delete a book by its ID.",
    #     tags=["Books"],
    #     responses={204: None},  # No content for DELETE
    # )
    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)


# def
class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
