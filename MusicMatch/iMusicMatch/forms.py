from django import forms
from django.contrib.auth.models import User as Django_User
from .models import *

class PostFormGroupReview(forms.ModelForm):

    class Meta:
        model = GroupReview
        fields = ('groupID','review',)

class PostFormPlaylistReview(forms.ModelForm):

    class Meta:
        model = PlaylistReview
        fields = ('playlistID','review',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('scID','name','userList',)

class EditPlaylistReviewForm(forms.ModelForm):

    class Meta:
        model = PlaylistReview
        fields = ('review',)

class EditGroupReviewForm(forms.ModelForm):

    class Meta:
        model = GroupReview
        fields = ('review',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Django_User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('realName',)
