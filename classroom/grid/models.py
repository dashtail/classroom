from django.db import models
from classroom.course.models import Course


class Grid(models.Model):
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course, related_name="grids_courses")

    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Grades"

    def __str__(self):
        return self.name
