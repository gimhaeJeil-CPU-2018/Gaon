from django import forms
from .models import BoothList, photo
from django.contrib.auth.models import User

class BoothForm(forms.ModelForm):
    class Meta:
        model = BoothList
        fields = ('stxt', 'text', 'floor', 'location',)

class ImageAdd(forms.ModelForm):
    class Meta:
        model = photo
        fields = ('img',)

class JoinNew(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class LoginGo(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')