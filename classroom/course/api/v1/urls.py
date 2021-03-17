from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CourseDetail, CourseList

urlpatterns = [
    path("courses/", CourseList.as_view()),
    path("courses/<int:pk>/", CourseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)