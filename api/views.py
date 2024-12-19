from django.shortcuts import render
from drf_spectacular.utils import extend_schema
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
from config.exceptions import ClientError


# Create your views here.

class TestAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Test 조회",
        description="Test 조회중 입니다.",
        responses={
            200: TestSerializer(many=True)
        }
    )
    def get(self, request):
        test = Test.objects.all()
        serializer = TestSerializer(test, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Test 생성",
        description="Test 생성중 입니다.",
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

class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

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
        raise ClientError()
        # raise ValidationError("잘못된 요청입니다.")
