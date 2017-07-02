from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from creator.models import Form
from creator.views import get_all_fields, login_user

from .models import TextFieldInput, NumericFieldInput, DateFieldInput, MemoFieldInput, MCQFieldInput
from .forms import TextFieldInputForm, NumericFieldInputForm, DateFieldInputForm, MemoFieldInputForm, MCQFieldInputForm


def display_form(request, form_id, sr_no):
    if not request.user.is_authenticated():
        return render(request, 'creator/login.html')

    # todo clean up code
    current_form = get_object_or_404(Form, pk=form_id)
    if not current_form.deployed:
        current_form.deployed = True
        current_form.save()
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
        form = TextFieldInputForm(request.POST or None)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.parent_field = current_field
            answer.save()
            if last:
                forms = Form.objects.filter(user=request.user)
                return render(request, 'creator/index.html', {'forms': forms, })
            else:
                return redirect('input:display_form', form_id=form_id, sr_no=sr_no+1)

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

    if current_field_type == 'NumericField':
        numeric_field_input = NumericFieldInput()
        numeric_field_input.parent_field = current_field
        form = NumericFieldInputForm(request.POST or None, instance=numeric_field_input)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.save()
            if last:
                forms = Form.objects.filter(user=request.user)
                return render(request, 'creator/index.html', {'forms': forms, })
            else:
                return redirect('input:display_form', form_id=form_id, sr_no=sr_no+1)

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

    if current_field_type == 'DateField':
        date_field_input = DateFieldInput()
        date_field_input.parent_field = current_field
        form = DateFieldInputForm(request.POST or None, instance=date_field_input)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.save()
            if last:
                forms = Form.objects.filter(user=request.user)
                return render(request, 'creator/index.html', {'forms': forms, })
            else:
                return redirect('input:display_form', form_id=form_id, sr_no=sr_no+1)

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

    if current_field_type == 'MemoField':
        memo_field_input = MemoFieldInput()
        memo_field_input.parent_field = current_field
        form = MemoFieldInputForm(request.POST or None, instance=memo_field_input)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.save()
            if last:
                forms = Form.objects.filter(user=request.user)
                return render(request, 'creator/index.html', {'forms': forms, })
            else:
                return redirect('input:display_form', form_id=form_id, sr_no=sr_no+1)

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

    if current_field_type == 'MCQField':
        mcq_field_input = MCQFieldInput()
        mcq_field_input.parent_field = current_field
        form = MCQFieldInputForm(request.POST or None, instance=mcq_field_input)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.save()
            if last:
                forms = Form.objects.filter(user=request.user)
                return render(request, 'creator/index.html', {'forms': forms, })
            else:
                return redirect('input:display_form', form_id=form_id, sr_no=sr_no+1)

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
