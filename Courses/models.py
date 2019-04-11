from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Course(models.Model):
    course_title = models.CharField(max_length=200, blank=False, null=False)
    course_code = models.CharField(max_length=20, unique=True)
    credit = models.IntegerField(validators=[MinValueValidator(1),])

    def __str__(self):
        return self.course_title+" "+self.course_code