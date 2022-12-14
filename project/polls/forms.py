from django import forms
from .models import PostList


class UserForm(forms.ModelForm):
    class Meta:
        model = PostList
        fields = '__all__'