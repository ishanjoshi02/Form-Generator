import datetime
from django import forms

from .models import TextFieldInput, NumericFieldInput, DateFieldInput, MemoFieldInput, MCQFieldInput
from creator.models import TextField, NumericField, DateField, MemoField, MCQField


class TextFieldInputForm(forms.ModelForm):
    class Meta:
        model = TextFieldInput
        fields = [
            'answer',
        ]


class NumericFieldInputForm(forms.ModelForm):
    class Meta:
        model = NumericFieldInput
        fields = [
            'answer',
        ]


class DateFieldInputForm(forms.ModelForm):
    answer = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1980, 2018)
    ))

    class Meta:
        model = DateFieldInput
        fields = [
            'answer',
        ]


class MemoFieldInputForm(forms.ModelForm):
    answer = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = MemoFieldInput
        fields = [
            'answer',
        ]


class MCQFieldInputForm(forms.ModelForm):
    answer = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple())

    # todo add choices in init function

    class Meta:
        model = MCQFieldInput
        fields = [
            'answer',
        ]
