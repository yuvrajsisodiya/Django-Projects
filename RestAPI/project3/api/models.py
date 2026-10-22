from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    qualifecation = models.CharField(max_length=100)
    age = models.IntegerField()

    def __st__(self):
        return name
