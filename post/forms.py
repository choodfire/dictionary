from django import forms
from .models import Post
from django.forms import ModelForm

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()

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