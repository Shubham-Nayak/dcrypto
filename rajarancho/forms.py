from django import forms
from .models import AllData

# class PswdForm(forms.Form):
#     finder = forms.CharField(widget=forms.TextInput(attrs={
#         'type': 'password',
#         'id': 'password',
#         'class': 'validate'
#     }))

class EncryptForm(forms.Form):
    decText = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control ',
        'id': 'exampleFormControlTextarea1',
        'rows': '5',
        'data-length': '5000',
    }))
    finder = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password ',
        'id': 'exampleInputPassword1',
        'class': 'form-control pass',
        'placeholder':'Protect Data With Password.'
    }))

class DecryptForm(forms.Form):
    encText = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control ',
        'id': 'exampleFormControlTextarea1',
        'rows': '5',
        'data-length': '5000',
    }))
    finder = forms.CharField(widget=forms.TextInput(attrs={
          'type': 'password ',
        'id': 'exampleInputPassword1',
        'class': 'form-control pass',
        'placeholder':'Protect Data With Password.'
    }))