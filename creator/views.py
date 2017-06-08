from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .forms import FormForm, UserForm, TextFieldForm
from .models import Form, TextField


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

            fields = TextField.objects.filter(parent_form=field.parent_form).order_by('sr_no')

            return render(request, 'creator/detail.html', context={
                'form':
                    field.parent_form,
                'user':
                    user,
                'fields':
                    fields
            })
        context = {
            'form':
                form
        }
        return render(request, 'creator/create_text_field.html', context=context)


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

            return render(request, 'creator/index.html')
        context = {
            'form':
                form
        }
        return render(request, 'creator/create_form.html', context)


def detail(request, form_id):
    if not request.user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
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


def delete_form(request, form_id):
    current_form = Form.objects.get(pk=form_id)
    current_form.delete()
    forms = Form.objects.filter(user=request.user)
    return render(request, 'creator/index.html', {
        'forms':
            forms
    })


def edit_form(request, form_id):
    if not request.user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
        current_form = Form.objects.get(pk=form_id)
        form = FormForm(request.POST or None, instance=current_form)
        if form.is_valid():
            current_form = form.save(commit=False)
            current_form.user = request.user
            current_form.save()

            user = request.user
            current_form = get_object_or_404(Form, pk=form_id)
            context = {
                'form':
                    current_form,
                'user':
                    user
            }
            return render(request, 'creator/detail.html', context)
        context = {
            'form':
                form
        }
        return render(
            request,
            'creator/edit_form.html',
            context=context
        )


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
                return render(request, 'creator/index.html')
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
