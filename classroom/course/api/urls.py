from django.urls import path, include
from classroom.course.api.v1 import urls

urlpatterns = [
    path("v1/", include((urls, "v1"), namespace="v1")),
]
