from django import forms
from .models import King

class KingForm(forms.Form):
    name= forms.CharField(max_length=20, widget=forms.TextInput(attrs={'name':'name'}))
    pic=forms.ImageField(widget=forms.FileInput(attrs={'name':'name','type':'file'}))