from django.urls import path, include
from classroom.course.api.v1 import urls

urlpatterns = [
    path("api/", include((urls, "api_course"), namespace="course_url")),
]
