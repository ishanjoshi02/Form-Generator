from __future__ import unicode_literals

from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import render, get_object_or_404, redirect
from creator.models import Form, TextField, DateField, MCQField, NumericField, MemoField
from creator.views import get_all_fields, login_user

from .models import TextFieldInput, NumericFieldInput, DateFieldInput, MemoFieldInput, MCQFieldInput
from .forms import TextFieldInputForm, NumericFieldInputForm, DateFieldInputForm, MemoFieldInputForm, MCQFieldInputForm


def display_form(request, form_id, sr_no):
    current_form = Form.objects.get(pk=form_id)
    current_fields = get_all_fields(current_form)
    forms = []
    if request.method == "POST":
        pass
    else:
        for field in current_fields:
            if type(field) is TextField:
                pass
            elif type(field) is NumericField:
                pass
            elif type(field) is MemoField:
                pass
            elif type(field) is MCQField:
                pass
            else:
                form = DateFieldInputForm(prefix=str(field.caption))
                form.fields['answer'].required = field.required
                form.fields['answer'].widget.years = range(field.date_low.year,field.date_high.year)