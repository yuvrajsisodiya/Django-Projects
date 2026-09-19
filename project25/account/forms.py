from django.forms import ModelForm
from .models import upload_files
from django import forms
class upload_file_form(forms.ModelForm):
    class Meta:
        model = upload_files
        fields = '__all__'