from django import forms
from .models import Post
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'text', 'image')
        labels = {
            'title': '',
            'description': '',
            'text': '',
            'image': ''
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post title'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Short description'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Main text'}),
        }