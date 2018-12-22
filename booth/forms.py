from django import forms
from .models import BoothList

class BoothForm(forms.ModelForm):
    class meta:
        model = BoothList
        fields = ('BthName', 'stxt', 'text', 'floor', 'location', )