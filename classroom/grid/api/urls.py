from django.urls import path, include
from classroom.grid.api.v1 import urls

urlpatterns = [
    path("v1/", include((urls, "v1"), namespace="v1")),
]
