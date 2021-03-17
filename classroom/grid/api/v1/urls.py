from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GridList, GridDetail

urlpatterns = [
    path("grids/", GridList.as_view()),
    path("grids/<int:pk>/", GridDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)