from django import forms
from .models import Post
class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg',
                    'placeholder': 'Enter post title'
                }
            ),

            'content': forms.Textarea(
                attrs={
                    'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg',
                    'placeholder': 'Write your post content...',
                    'rows': 8
                }
            ),
        }