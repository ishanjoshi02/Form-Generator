import datetime
from django import forms

from .models import TextFieldInput, NumericFieldInput, DateFieldInput, MemoFieldInput, MCQFieldInput
from creator.models import TextField, NumericField, DateField, MemoField, MCQField


class TextFieldInputForm(forms.ModelForm):
    answer = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(TextFieldInputForm, self).__init__(*args, **kwargs)
        self.fields['answer'].required = False

    class Meta:
        model = TextFieldInput
        fields = [
            'answer',
        ]


class NumericFieldInputForm(forms.ModelForm):
    answer = forms.IntegerField()

    class Meta:
        model = NumericFieldInput
        fields = [
            'answer',
        ]


class DateFieldInputForm(forms.ModelForm):
    answer = forms.DateField(widget=forms.SelectDateWidget(
        years=range(0, 3000)
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

    class Meta:
        model = MCQFieldInput
        fields = [
            'answer',
        ]
