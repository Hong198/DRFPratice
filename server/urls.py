from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    # in app
    path("api/", include('api.urls')),
    path("book/", include('book.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += [
    path("openapi/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "openapi/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "openapi/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
