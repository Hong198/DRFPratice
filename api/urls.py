from os.path import basename

from django.urls import path, include
from rest_framework import routers

from api.views import TestAPIView, TestViewSet, TestView

router = routers.DefaultRouter()
router.register(r"tests", TestViewSet, basename='tests')

app_name = 'api'
urlpatterns = [
    path("", include(router.urls)),
    #
    path("test/", TestAPIView.as_view(), name='test-list'),
    #
    # path("testlist/", TestListAPIVIew.as_view(), name="tests-list"),
    # path("testlist/<int:pk>/", TestDetailAPIVIew.as_view(), name="tests-detail"),
    #
    path("hello/",TestView.as_view(), name='tests'),
]
