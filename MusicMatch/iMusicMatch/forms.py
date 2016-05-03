from django import forms
from django.contrib.auth.models import User as Django_User
from .models import *

class PostForm(forms.ModelForm):

        class Meta:
            model = Group
            fields = ('scID','name','userList',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Django_User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('realName',)
