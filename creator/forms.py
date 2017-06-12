from django import forms
from django.contrib.auth.models import User
from .models import DateField, Form, TextField, NumericField


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class FormForm(forms.ModelForm):
    body_text = forms.CharField(widget=forms.Textarea)

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


class NumericFieldForm(forms.ModelForm):
    class Meta:
        model = NumericField
        fields = [
            'sr_no',
            'caption',
            'question',
            'required',
            'range_high',
            'range_low',
            'decimal_places',
        ]

class DateFieldForm(forms.Form):
    class Meta:
        model = DateField
        fields = [
            'sr_no',
            'caption',
            'question',
            'required',
            'date_high',
            'date_low'
        ]
