from django.db import models
# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=50)
    fee = models.IntegerField()

def __str__(self):
    return self.name