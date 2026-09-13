from django import forms
from .models import Employe
class emp_form(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['name','age','email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border p-2 rounded w-full hover:border-blue-400 transitions duration-200 border-2 mt-2 mb-2 shadow-lg',
                'placeholder': 'Enter employee name....'
            }),

            'age': forms.NumberInput(attrs={
                'class': 'border p-2 rounded w-full  hover:border-blue-400 transitions duration-200 border-2 mt-2 mb-2 shadow-lg',
                'placeholder': 'Enter employee age'
            }),
            'email': forms.TextInput(attrs={
                'class': 'border p-2 rounded w-full  hover:border-blue-400 transitions duration-200 border-2 mt-2 mb-2 shadow-lg',
                'placeholder': 'Enter employee email'
            }),
        }
        # labels = {
        #     'name': 'Employee Name',
        #     'age': 'Employee Age',
        #     }
        # help_texts = {
        #     'name':'Please enter full name',
        #     'age':'Please enter age',
        # }
        # custome validations 
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Age must be at least 18')
        return age
            
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.replace(" ","").isalpha():
            raise forms.ValidationError('Name must contain only letters and spaces.')
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError(
                'Email must be a Gmail address.'
            )

        return email