from django.db import models

# Create your models here.
from django.db import models
class students(models.Model):
      name=models.CharField(max_length=100)
      age=models.IntegerField()
      city=models.CharField(max_length=20)
      email=models.EmailField(unique=True)
      Mob_no = models.IntegerField()

