from django.forms import ModelForm
from .models import Student
class stdform(ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','age']
        