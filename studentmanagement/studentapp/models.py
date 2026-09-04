from django.db import models

# Create your models here.
class Student(models.Model):
    
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    date  = models.DateField(auto_now_add=True)
    mob = models.IntegerField()
    

    def __str__(self):
        return self.name