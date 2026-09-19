
from django import forms
# import models class
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Enter post title'
            }),

            'content': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 h-40 focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Write your post content...'
            }),
        }