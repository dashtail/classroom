from django.urls import path, include
from classroom.grid.api.v1 import urls

urlpatterns = [
    path("api/", include((urls, "api_grid"), namespace="grids_url")),
]
