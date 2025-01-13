from django.urls import path, include
from rest_framework import routers

from .views import BookModelViewSet, BookListAPIView, BookDetailAPIView, ExampleView

router = routers.DefaultRouter()
router.register(r'books', BookModelViewSet, basename="books")

app_name="book"
urlpatterns = [
    path("", include(router.urls)),
    #
    path("book/", BookListAPIView.as_view(), name="book-list"),
    path("book/<int:pk>/", BookDetailAPIView.as_view(), name="book-detail"),
    #
    path("hello/", ExampleView.as_view(), name='hello'),
]
