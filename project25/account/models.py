from django.db import models

# Create your models here.
class upload_files(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    # document = models.FileField(upload_to='documents/')
