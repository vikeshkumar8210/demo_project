

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.roll_number})"



