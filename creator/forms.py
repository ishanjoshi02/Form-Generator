from django import forms
from django.contrib.auth.models import User
from .models import Form, TextField


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = [
            'form_name',
            'header_text',
            'body_text'
        ]


class TextFieldForm(forms.ModelForm):
    class Meta:
        model = TextField
        fields = [
            'sr_no',
            'caption',
            'question',
            'required',
        ]
