from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=75)
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.name
