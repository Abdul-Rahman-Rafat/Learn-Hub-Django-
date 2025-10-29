from django.db import models
from student.models import Student

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return self.name
    

