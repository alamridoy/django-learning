from django.db.models import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        

class BlogPostForm(froms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'