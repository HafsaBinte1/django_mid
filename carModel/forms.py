from django import forms
from .models import Comment


class cmtf(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']
