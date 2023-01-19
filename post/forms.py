from django import forms
from .models import Post

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()