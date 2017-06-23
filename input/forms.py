from django import forms

from .models import TextFieldInput, NumericFieldInput, DateFieldInput, MemoFieldInput, MCQFieldInput
from creator.models import TextField, NumericField, DateField, MemoField, MCQField


class TextFieldInputForm(forms.ModelForm):
    class Meta:
        model = TextFieldInput
        fields = [
            'answer',
        ]
