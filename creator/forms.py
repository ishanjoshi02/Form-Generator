from django import forms
from django.contrib.auth.models import User
from .models import DateField, Form, TextField, NumericField, MemoField, MCQField


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


class DateFieldForm(forms.ModelForm):
    date_high = forms.DateInput()
    date_low = forms.DateInput()

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


class MemoFieldForm(forms.ModelForm):
    class Meta:
        model = MemoField
        fields = [
            'sr_no',
            'caption',
            'question',
            'required',
        ]


class MCQFieldForm(forms.ModelForm):
    # choices = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder':'Choice'}))
    class Meta:
        model = MCQField
        fields = [
            'sr_no',
            'caption',
            'question',
            'required',
            'choices'
        ]
