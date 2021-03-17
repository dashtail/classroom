from rest_framework import serializers
from classroom.course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "description",
        ]
