# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.forms import formset_factory
from creator.models import Form
from creator.views import get_all_fields, login_user

from .models import TextFieldInput
from .forms import TextFieldInputForm


def display_form(request, form_id, sr_no):
    if not request.user.is_authenticated():
        return render(request, 'creator/login.html')

    current_form = get_object_or_404(Form, pk=form_id)
    # todo set current form's deployed status to true
    fields = get_all_fields(current_form)
    sr_no = int(sr_no)
    list_length = len(fields)
    if list_length < sr_no:
        forms = Form.objects.filter(user=request.user)
        return render(request, 'creator/index.html', {'forms': forms, })
    current_field = fields[sr_no - 1]
    current_field_type = current_field.get_model_type()
    last = sr_no == list_length
    button_text = 'Submit' if last else 'Next'
    if current_field_type == 'TextField':
        text_field_input = TextFieldInput()
        text_field_input.parent_text_field = current_field
        form = TextFieldInputForm(request.POST or None, instance=text_field_input)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.save()
            if last:
                forms = Form.objects.filter(user=request.user)
                return render(request, 'creator/index.html', {'forms': forms, })
            else:
                pass

        sr_no += 1
        context = {
            'form':
                form,
            'button_text':
                button_text,
            'header_text':
                current_field.question,
            'current_form':
                current_form,
            'sr_no':
                sr_no,
        }
        return render(request, 'input/display_form.html', context)
