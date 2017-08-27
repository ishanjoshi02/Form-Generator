import operator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .forms import DateFieldForm, FormForm, UserForm, TextFieldForm, NumericFieldForm, MCQFieldForm, MemoFieldForm
from .models import DateField, Form, TextField, NumericField, MemoField, MCQField
from input.models import TextFieldInput, NumericFieldInput, DateFieldInput, MCQFieldInput, MemoFieldInput


def create_date_field(request, form_id):
    form = DateFieldForm(request.POST or None)
    if form.is_valid():
        field = form.save(commit=False)
        field.parent_form = Form.objects.get(pk=form_id)
        field.save()
        context = {
            'form':
                field.parent_form,
            'user':
                request.user,
            'fields':
                get_all_fields(field.parent_form)
        }
        return render(request, 'creator/detail.html', context=context)
    context = {
        'form':
            form,
        'header_text':
            'Add a Date Field',
        'button_text':
            'Add Date Field'
    }
    return render(request, 'creator/create_form.html', context=context)


def create_text_field(request, form_id):
    form = TextFieldForm(request.POST or None)
    if form.is_valid():
        field = form.save(commit=False)
        field.parent_form = Form.objects.get(pk=form_id)
        field.save()
        return render(request, 'creator/detail.html', context={
            'form':
                field.parent_form,
            'user':
                request.user,
            'fields':
                get_all_fields(field.parent_form)
        })
    context = {
        'form':
            form,
        'header_text':
            'Add a Text Field',
        'button_text':
            'Add Text Field'
    }
    return render(request, 'creator/create_form.html', context=context)


def create_mcq_field(request, form_id):
    form = MCQFieldForm(request.POST or None)
    if form.is_valid():
        field = form.save(commit=False)
        field.parent_form = Form.objects.get(pk=form_id)
        field.save()
        context = {
            'form':
                field.parent_form,
            'user':
                request.user,
            'fields':
                get_all_fields(field.parent_form),
        }
        return render(request, 'creator/detail.html', context=context)
    return render(request, 'creator/create_form.html',
                  context={'form': form, 'header_text': 'Add a MCQ Field', 'button_text': 'Add Field'})


def create_memo_field(request, form_id):
    form = MemoFieldForm(request.POST or None)
    if form.is_valid():
        field = form.save(commit=False)
        field.parent_form = Form.objects.get(pk=form_id)
        field.save()
        context = {
            'form':
                field.parent_form,
            'user':
                request.user,
            'fields':
                get_all_fields(field.parent_form),
        }
        return render(request, 'creator/detail.html', context=context)
    context = {
        'header_text':
            'Add a Memo Field',
        'button_text':
            'Add Field',
        'form':
            form,
    }
    return render(request, 'creator/create_form.html', context=context)


def create_numeric_field(request, form_id):
    form = NumericFieldForm(request.POST or None)
    if form.is_valid():
        field = form.save(commit=False)
        field.parent_form = Form.objects.get(pk=form_id)
        field.save()
        context = {
            'form':
                field.parent_form,
            'user':
                user,
            'fields':
                get_all_fields(field.parent_form),
        }
        return render(request, 'creator/detail.html', context)
    return render(
        request,
        'creator/create_form.html',
        {
            'form':
                form,
            'header_text':
                'Add a Numeric Field',
            'button_text':
                'Add Numeric Field'
        }
    )


def create_form(request):
    form = FormForm(request.POST or None)
    if form.is_valid():
        mform = form.save(commit=False)
        mform.user = request.user
        mform.save()
        all_forms = Form.objects.filter(user=request.user)
        return render(request, 'creator/index.html', {
            'forms':
                all_forms
        })
    context = {
        'form':
            form,
        'header_text':
            'Add new Form',
        'button_text':
            'Create Form'
    }
    return render(request, 'creator/create_form.html', context)


def detail(request, form_id):
    user = request.user
    current_form = get_object_or_404(Form, pk=form_id)
    context = {
        'form':
            current_form,
        'user':
            user,
        'fields':
            get_all_fields(current_form),
      }
    return render(request, 'creator/detail.html', context)


def delete_form(request, form_id):
    Form.objects.get(pk=form_id).delete()
    forms = Form.objects.filter(user=request.user)
    return render(request, 'creator/index.html', {
        'forms':
            forms
    })


def delete_date_field(request, form_id, field_id):
    DateField.objects.get(pk=field_id).delete()
    current_form = get_object_or_404(Form, pk=form_id)
    context = {
        'form':
            current_form,
        'user':
            request.user,
        'fields':
            get_all_fields(current_form),
    }

    return render(request, 'creator/detail.html', context=context)


def delete_text_field(request, form_id, field_id):
    TextField.objects.get(pk=field_id).delete()
    current_form = get_object_or_404(Form, pk=form_id)
    context = {
        'form':
            current_form,
        'user':
            request.user,
        'fields':
            get_all_fields(current_form),
    }

    return render(request, 'creator/detail.html', context=context)


def delete_memo_field(request, form_id, field_id):
    MemoField.objects.get(pk=field_id).delete()
    current_form = get_object_or_404(Form, pk=form_id)
    context = {
        'form':
            current_form,
        'user':
            request.user,
        'fields':
            get_all_fields(current_form),
    }
    return render(request, 'creator/detail.html', context=context)


def delete_mcq_field(request, form_id, field_id):
    MCQField.objects.get(pk=field_id).delete()
    current_form = get_object_or_404(Form, pk=form_id)
    context = {
        'form':
            current_form,
        'user':
            request.user,
        'fields':
            get_all_fields(current_form),
    }
    return render(request, 'creator/detail.html', context=context)


def delete_numeric_field(request, form_id, field_id):
    NumericField.objects.get(pk=field_id).delete()
    current_form = get_object_or_404(Form, pk=form_id)
    context = {
        'form':
            current_form,
        'user':
            request.user,
        'fields':
            get_all_fields(current_form)
    }
    return render(request, 'creator/detail.html', context)


def edit_form(request, form_id):
    # todo change form of all fields to new field
    previous_form = Form.objects.get(pk=form_id)
    form = FormForm(request.POST or None, instance=previous_form)
    if form.is_valid():
        current_form = form.save(commit=False)
        current_form.user = request.user
        current_form.save()
        current_form = get_object_or_404(Form, pk=form_id)
        all_fields = list(TextField.objects.filter(parent_form=current_form).order_by('sr_no'))
        context = {
            'form':
                current_form,
            'user':
                request.user,
            'fields':
                all_fields,
        }
        return render(request, 'creator/detail.html', context)
    context = {
        'form':
            form,
        'header_text':
            'Edit ' + previous_form.form_name,
        'button_text':
            'Save Form'
    }
    return render(request, 'creator/create_form.html', context=context)


def edit_date_field(request, field_id):
    previous_field = DateField.objects.get(pk=field_id)
    form = DateFieldForm(request.POST or None, instance=previous_field)
    if form.is_valid():
        current_field = form.save(commit=False)
        current_field.parent_form = previous_field.parent_form
        current_field.save()
        context = {
            'form':
                previous_field.parent_form,
            'user':
                request.user,
            'fields':
                get_all_fields(previous_field.parent_form),
        }
        return render(request, 'creator/detail.html', context=context)
    context = {
        'form':
            form,
        'title':
            'Edit ' + previous_field.caption,
        'header_text':
            'Edit ' + previous_field.caption,
        'button_text':
            'Save',
    }
    return render(request, 'creator/create_form.html', context=context)


def edit_text_field(request, field_id):
    previous_field = TextField.objects.get(pk=field_id)
    form = TextFieldForm(request.POST or None, instance=previous_field)
    if form.is_valid():
        current_field = form.save(commit=False)
        current_field.parent_form = previous_field.parent_form
        current_field.save()
        context = {
            'form':
                previous_field.parent_form,
            'user':
                request.user}
        return render(request, 'creator/detail.html', context=context)
    context = {
        'form':
            form,
        'title':
            'Edit ' + previous_field.caption,
        'header_text':
            'Edit ' + previous_field.caption,
        'button_text':
            'Save'
    }
    return render(request, 'creator/create_form.html', context=context)


def edit_memo_field(request, field_id):
    previous_field = MemoField.objects.get(pk=field_id)
    form = MemoFieldForm(request.POST or None, instance=previous_field)
    if form.is_valid():
        current_field = form.save(commit=False)
        current_field.parent_form = previous_field.parent_form
        current_field.save()
        context = {
            'form':
                previous_field.parent_form,
            'user':
                request.user,
            'fields':
                get_all_fields(previous_field.parent_form),
        }
        return render(request, 'creator/detail.html', context=context)
    context = {
        'form':
            form,
        'title':
            'Edit ' + previous_field.caption,
        'header_text':
            'Edit ' + previous_field.caption,
        'button_text':
            'Save',
    }
    return render(request, 'creator/create_form.html', context=context)


def edit_mcq_field(request, field_id):
    previous_field = MCQField.objects.get(pk=field_id)
    form = MCQFieldForm(request.POST or None, instance=previous_field)
    if form.is_valid():
        current_field = form.save(commit=False)
        current_field.parent_form = previous_field.parent_form
        current_field.save()
        context = {
            'form':
                previous_field.parent_form,
            'user':
                request.user,
            'fields':
                get_all_fields(previous_field.parent_form),
        }
        return render(request, 'creator/detail.html', context=context)
    context = {
        'form':
            form,
        'title':
            'Edit ' + previous_field.caption,
        'header_text':
            'Edit ' + previous_field.caption,
        'button_text':
            'Save',
    }
    return render(request, 'creator/create_form.html', context=context)


def edit_numeric_field(request, field_id):
    previous_field = NumericField.objects.get(pk=field_id)
    form = NumericFieldForm(request.POST or None, instance=previous_field)
    if form.is_valid():
        current_field = form.save(commit=False)
        current_field.parent_form = previous_field.parent_form
        current_field.save()
        context = {
            'form':
                previous_field.parent_form,
            'user':
                request.user,
            'fields':
                get_all_fields(previous_field.parent_form),
        }
        return render(request, 'creator/detail.html', context=context)
    context = {
        'form':
            form,
        'title':
            'Edit ' + previous_field.caption,
        'header_text':
            'Edit ' + previous_field.caption,
        'button_text':
            'Save',
    }
    return render(request, 'creator/create_form.html', context=context)


def get_all_fields(form):
    fields = []
    text_fields = list(TextField.objects.filter(parent_form=form))
    if text_fields.__len__() >= 1:
        fields += text_fields
    elif text_fields.__len__() == 1:
        fields.append(text_fields)
    numeric_fields = list(NumericField.objects.filter(parent_form=form))
    if numeric_fields.__len__() >= 1:
        fields += numeric_fields
    elif numeric_fields.__len__() == 1:
        fields.append(numeric_fields)
    date_fields = list(DateField.objects.filter(parent_form=form))
    if date_fields.__len__() >= 1:
        fields += date_fields
    elif date_fields.__len__() == 1:
        fields.append(date_fields)
    memo_fields = list(MemoField.objects.filter(parent_form=form))
    if memo_fields.__len__() >= 1:
        fields += memo_fields
    elif memo_fields.__len__() == 1:
        fields.append(memo_fields)
    mcq_fields = list(MCQField.objects.filter(parent_form=form))
    if mcq_fields.__len__() >= 1:
        fields += mcq_fields
    elif mcq_fields.__len__() == 1:
        fields.append(mcq_fields)

    return fields

def index(request):
    all_forms = Form.objects.filter(user=request.user)
    query = request.GET.get("q")
    if query:
        all_forms = all_forms.filter(
            Q(form_name__icontains=query) |
            Q(header_text__icontains=query)
        ).distinct
    return render(request, 'creator/index.html', {
        'forms': all_forms
    })


def login_user(request):
    if request.method == "POST":
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context = {
                    'forms':
                        Form.objects.filter(user=request.user)
                }
                return render(request, 'creator/index.html', context=context)
            else:
                return render(request, 'creator/login.html', context={
                    'error_message':
                        'Your account has been disabled'
                })
        else:
            return render(request, 'creator/login.html', {'error_message': 'Invalid Login'})
    return render(request, 'creator/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        'form':
            form
    }
    return render(request, 'creator/login.html', context=context)


def register_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request=request, user=user)
                return render(request, 'creator/index.html')
    context = {
        "form": form
    }
    return render(request, 'creator/register.html', context=context)


def result(request, form_id):
    current_form = Form.objects.get(pk=form_id)
    all_fields = get_all_fields(current_form)
    data = {}
    for field in all_fields:
        if type(field) == TextField:
            data[field.caption] = list(TextFieldInput.objects.filter(parent_field=field))
        elif type(field) == NumericField:
            data[field.caption] = list(NumericFieldInput.objects.filter(parent_field=field))
        elif type(field) == DateField:
            data[field.caption] = list(DateFieldInput.objects.filter(parent_field=field))
        elif type(field) == MemoField:
            data[field.caption] = list(MemoFieldInput.objects.filter(parent_field=field))
        else:
            data[field.caption] = list(MCQFieldInput.objects.filter(parent_field=field))
    columns = [data[field.caption] for field in all_fields]
    max_len = len(max(columns, key=len))
    for col in columns:
        col += [None,] * (max_len - len(col))
    rows = [[col[i] for col in columns] for i in range(max_len)]
    context = {
        'fields':
            all_fields,
        'data':
            rows
    }
    return render(request, 'creator/result.html', context=context)


def textFieldResult(request, field_id):
    current_field = TextField.objects.get(pk=field_id)
    results = (TextFieldInput.objects.filter(parent_field=current_field))
    query = request.GET.get("q")
    if query:
        results = results.filter(
            Q(form_name__icontains=query) |
            Q(header_text__icontains=query)
        ).distinct
    context = {
        'field':
            current_field,
        'results':
            results,
        'action':
            "{% url 'creator:text_field_result' %}",
    }
    return render(request, 'creator/field_result.html', context=context)


def numericFieldResult(request, field_id):
    current_field = NumericField.objects.get(pk=field_id)
    results = (NumericFieldInput.objects.filter(parent_field=current_field))
    query = request.GET.get("q")
    if query:
        results = results.filter(
            Q(form_name__icontains=query) |
            Q(header_text__icontains=query)
        ).distinct
    context = {
        'field':
            current_field,
        'results':
            results,
        'action':
            "{% url 'creator:numeric_field_result' %}",
    }
    return render(request, 'creator/field_result.html', context=context)


def dateFieldResult(request, field_id):
    current_field = DateField.objects.get(pk=field_id)
    results = (DateFieldInput.objects.filter(parent_field=current_field))
    query = request.GET.get("q")
    if query:
        results = results.filter(
            Q(form_name__icontains=query) |
            Q(header_text__icontains=query)
        ).distinct
    context = {
        'field':
            current_field,
        'results':
            results,
        'action':
            "{% url 'creator:date_field_result' %}",
    }
    return render(request, 'creator/field_result.html', context=context)


def memoFieldResult(request, field_id):
    current_field = MemoField.objects.get(pk=field_id)
    results = MemoFieldInput.objects.filter(parent_field=current_field)
    query = request.GET.get("q")
    if query:
        results = results.filter(
            Q(form_name__icontains=query) |
            Q(header_text__icontains=query)
        ).distinct
    context = {
        'field':
            current_field,
        'results':
            results,
        'action':
            "{% url 'creator:memo_field_result' %}",
    }
    return render(request, 'creator/field_result.html', context=context)


def mcqFieldResult(request, field_id):
    current_field = MCQField.objects.get(pk=field_id)
    results = (MCQFieldInput.objects.filter(parent_field=current_field))
    query = request.GET.get("q")
    if query:
        results = results.filter(
            Q(form_name__icontains=query) |
            Q(header_text__icontains=query)
        ).distinct
    context = {
        'field':
            current_field,
        'results':
            results,
        'action':
            "{% url 'creator:mcq_field_result' %}",
    }
    return render(request, 'creator/field_result.html', context=context)
