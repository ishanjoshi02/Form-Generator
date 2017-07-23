from __future__ import unicode_literals

from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import render, get_object_or_404, redirect
from creator.models import Form
from creator.views import get_all_fields, login_user

from .models import TextFieldInput, NumericFieldInput, DateFieldInput, MemoFieldInput, MCQFieldInput
from .forms import TextFieldInputForm, NumericFieldInputForm, DateFieldInputForm, MemoFieldInputForm, MCQFieldInputForm


def display_form(request, form_id, sr_no):
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
        form.fields['answer'].required = current_field.required

        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.parent_field = current_field
            answer.save()
            if last:
                forms = Form.objects.filter(user=request.user)
                return render(request, 'creator/index.html', {'forms': forms, })
            else:
                return redirect('input:display_form', form_id=form_id, sr_no=sr_no + 1)

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
        form.fields['answer'].required = current_field.required
        form.fields['answer'].validators = [
            MaxValueValidator(current_field.range_high),
            MinValueValidator(current_field.range_low)
        ]

        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.save()
            if last:
                forms = Form.objects.filter(user=request.user)
                return render(request, 'creator/index.html', {'forms': forms, })
            else:
                return redirect('input:display_form', form_id=form_id, sr_no=sr_no + 1)

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
        form = DateFieldInputForm(request.POST or None, )
        form.fields['answer'].required = current_field.required
        form.fields['answer'].widget.years = range(
            current_field.date_low.year,
            current_field.date_high.year,
        )

        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.parent_field = current_field
            answer.save()
            if last:
                forms = Form.objects.filter(user=request.user)
                return render(request, 'creator/index.html', {'forms': forms, })
            else:
                return redirect('input:display_form', form_id=form_id, sr_no=sr_no + 1)

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
        form = MemoFieldInputForm(request.POST or None)
        form.fields['answer'].required = current_field.required

        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.parent_field = current_field
            answer.save()
            if last:
                forms = Form.objects.filter(user=request.user)
                return render(request, 'creator/index.html', {'forms': forms, })
            else:
                return redirect('input:display_form', form_id=form_id, sr_no=sr_no + 1)

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
        form = MCQFieldInputForm(request.POST or None)
        form.fields['answer'].required = current_field.required
        choices = current_field.choices
        choices = choices.split(",")

        tuple_choices = []

        for choice in choices:
            choice = str(choice)

            tuple_choices += (choice, choice),

        form.fields['answer'].choices = tuple(tuple_choices)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.parent_field = current_field
            answer.save()
            if last:
                forms = Form.objects.filter(user=request.user)
                return render(request, 'creator/index.html', {'forms': forms, })
            else:
                return redirect('input:display_form', form_id=form_id, sr_no=sr_no + 1)

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
