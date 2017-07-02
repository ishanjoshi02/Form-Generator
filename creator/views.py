import operator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .forms import DateFieldForm, FormForm, UserForm, TextFieldForm, NumericFieldForm, MCQFieldForm, MemoFieldForm
from .models import DateField, Form, TextField, NumericField, MemoField, MCQField
from input.models import TextFieldInput, NumericFieldInput, DateFieldInput, MCQFieldInput, MemoFieldInput


def create_date_field(request, form_id):
    user = request.user
    if not user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
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
    user = request.user
    if not user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
        form = TextFieldForm(request.POST or None)

        if form.is_valid():
            field = form.save(commit=False)
            field.parent_form = Form.objects.get(pk=form_id)
            field.save()

            return render(request, 'creator/detail.html', context={
                'form':
                    field.parent_form,
                'user':
                    user,
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
    user = request.user
    if not user.is_authenticated():
        return render(request, 'creator/login.html')
    # todo change to custom template
    else:
        form = MCQFieldForm(request.POST or None)
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

            return render(request, 'creator/detail.html', context=context)
        return render(request, 'creator/create_form.html',
                      context={'form': form, 'header_text': 'Add a MCQ Field', 'button_text': 'Add Field'})


def create_memo_field(request, form_id):
    user = request.user
    if not user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
        form = MemoFieldForm(request.POST or None)
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
    user = request.user
    if not user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
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

            return render(request,
                          'creator/detail.html',
                          context
                          )
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
    user = request.user
    if not user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
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
    if not request.user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
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
    current_form = Form.objects.get(pk=form_id)
    current_form.delete()
    forms = Form.objects.filter(user=request.user)
    return render(request, 'creator/index.html', {
        'forms':
            forms
    })


def delete_date_field(request, form_id, field_id):
    current = DateField.objects.get(pk=field_id)
    current.delete()
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
    current = TextField.objects.get(pk=field_id)
    current.delete()
    current_form = get_object_or_404(Form, pk=form_id)
    context = {
        'form':
            current_form,
        'user':
            request.user,
        'fields':
            get_all_fields(current_form),
    }

    return render(request, 'creator/detail.html', context)


def delete_memo_field(request, form_id, field_id):
    user = request.user
    if not user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
        current = MemoField.objects.get(pk=field_id)
        current.delete()
        current_form = get_object_or_404(Form, pk=form_id)
        context = {
            'form':
                current_form,
            'user':
                user,
            'fields':
                get_all_fields(current_form),
        }

        return render(request, 'creator/detail.html', context=context)


def delete_mcq_field(request, form_id, field_id):
    user = request.user
    if not user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
        current = MCQField.objects.get(pk=field_id)
        current.delete()
        current_form = get_object_or_404(Form, pk=form_id)
        context = {
            'form':
                current_form,
            'user':
                user,
            'fields':
                get_all_fields(current_form),
        }

        return render(request, 'creator/detail.html', context=context)


def delete_numeric_field(request, form_id, field_id):
    current = NumericField.objects.get(pk=field_id)
    current.delete()
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
    if not request.user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
        # todo change form of all fields to new field
        previous_form = Form.objects.get(pk=form_id)
        form = FormForm(request.POST or None, instance=previous_form)
        if form.is_valid():
            current_form = form.save(commit=False)
            current_form.user = request.user
            current_form.save()

            user = request.user
            current_form = get_object_or_404(Form, pk=form_id)
            all_fields = list(TextField.objects.filter(parent_form=current_form).order_by('sr_no'))
            context = {
                'form':
                    current_form,
                'user':
                    user,
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
        return render(
            request,
            'creator/create_form.html',
            context=context
        )


def edit_date_field(request, field_id):
    if not request.user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
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

            return render(
                request,
                'creator/detail.html',
                context=context
            )
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
        return render(
            request,
            'creator/create_form.html',
            context=context
        )


def edit_text_field(request, field_id):
    if not request.user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
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
                    request.user
            }

            return render(
                request,
                'creator/detail.html',
                context=context
            )
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
        return render(
            request,
            'creator/create_form.html',
            context=context
        )


def edit_memo_field(request, field_id):
    if not request.user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
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
    user = request.user
    if not user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
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
                    user,
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
    user = request.user
    if not user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
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
                    user,
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

    text_fields = (TextField.objects.filter(parent_form=form))
    if type(text_fields) is list:
        for field in text_fields:
            fields += field
    else:
        fields += text_fields

    numeric_fields = list(NumericField.objects.filter(parent_form=form))
    if not numeric_fields.__len__() <= 1:
        for field in numeric_fields:
            fields += field
    else:
        fields += numeric_fields

    date_fields = list(DateField.objects.filter(parent_form=form))
    if not date_fields.__len__() <= 1:
        for field in date_fields:
            fields += field
    else:
        fields += date_fields

    memo_fields = list(MemoField.objects.filter(parent_form=form))
    if not memo_fields.__len__() <= 1:
        for field in memo_fields:
            fields += field
    else:
        fields += memo_fields

    mcq_fields = list(MCQField.objects.filter(parent_form=form))
    if not mcq_fields.__len__() <= 1:
        for field in mcq_fields:
            fields += field
    else:
        fields += mcq_fields

    # todo write code to sort the fields

    return fields


def index(request):
    if not request.user.is_authenticated():
        form = UserForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'creator/login.html', context=context)
    else:
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
    fields = get_all_fields(current_form)

    context = {
        'fields':
            fields,
    }
    return render(request, 'creator/result.html', context=context)


def textFieldResult(request, field_id):
    current_field = TextField.objects.get(pk=field_id)
    results = list(TextFieldInput.objects.filter(parent_field=current_field))

    context = {
        'field':
            current_field,
        'results':
            results,
    }
    return render(request, 'creator/field_result.html', context=context)


def numericFieldResult(request, field_id):
    current_field = NumericField.objects.get(pk=field_id)
    results = list(NumericFieldInput.objects.filter(parent_field=current_field))

    context = {
        'field':
            current_field,
        'results':
            results,
    }
    return render(request, 'creator/field_result.html', context=context)


def dateFieldResult(request, field_id):
    current_field = DateField.objects.get(pk=field_id)
    results = list(DateFieldInput.objects.filter(parent_field=current_field))

    context = {
        'field':
            current_field,
        'results':
            results,
    }
    return render(request, 'creator/field_result.html', context=context)


def memoFieldResult(request, field_id):
    current_field = MemoField.objects.get(pk=field_id)
    results = list(MemoFieldInput.objects.filter(parent_field=current_field))

    context = {
        'field':
            current_field,
        'results':
            results,
    }
    return render(request, 'creator/field_result.html', context=context)


def mcqFieldResult(request, field_id):
    current_field = MCQField.objects.get(pk=field_id)
    results = list(MCQFieldInput.objects.filter(parent_field=current_field))

    context = {
        'field':
            current_field,
        'results':
            results,
    }
    return render(request, 'creator/field_result.html', context=context)
