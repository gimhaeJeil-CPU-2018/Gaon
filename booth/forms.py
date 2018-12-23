from django import forms
from .models import BoothList, photo
from django.contrib.auth.models import User

class BoothForm(forms.ModelForm):
    class Meta:
        model = BoothList
        fields = ('BthName', 'picture', 'stxt', 'text', 'floor', 'location',)

class ImageAdd(forms.ModelForm):
    class Meta:
        model = photo
        fields = ('name', 'img',)

class JoinNew(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class LoginGo(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')