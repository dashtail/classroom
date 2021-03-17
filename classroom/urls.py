from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from classroom.grid import urls as grid_urls
from classroom.course import urls as course_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Classroom",
        default_version="v1",
        contact=openapi.Contact(email="rafaelbkbral@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include((grid_urls, "grid_api"), namespace="grid_api")),
    path("", include(course_urls)),
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
