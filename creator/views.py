import pyrebase
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render

from .forms import formForm, UserForm
from .models import Form


def create_form(request):
    if not request.user.is_authenticated():
        return render(request, 'creator/login.html')
    else:
        form = formForm(request.POST or None)
        if form.is_valid():
            mform = form.save(commit=False)
            mform.save()

            return render(request, 'creator/index.html')
        context = {
            'form':
                form
        }
        return render(request, 'creator/create_form.html', context)


def delete_form(request, form_id):
    current_form = Form.objects.get(pk=form_id)
    current_form.delete()
    forms = Form.objects.all()  # todo change to filter(user = request.user)
    return render(request, 'creator/index.html', {
        'forms':
            forms
    })


def index(request):
    if not request.user.is_authenticated():
        form = UserForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'creator/login.html', context=context)
    else:
        all_forms = Form.objects.all()
        return render(request, 'creator/index.html', {
            'forms': all_forms
        })


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        'form':
            form
    }
    return render(request, 'creator/login.html', context=context)


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


def init_firebase_database():
    config = {
        "apiKey": "AIzaSyC0BAl7F8ZdZx0afmnLgrbZeLDelm7sb0k",
        "authDomain": "forms-92fbf.firebaseapp.com",
        "databaseURL": "https://forms-92fbf.firebaseio.com",
        "projectId": "forms-92fbf",
        "storageBucket": "forms-92fbf.appspot.com",
        "messagingSenderId": "892199408538"
    }

    firebase = pyrebase.initialize_app(config)
    return firebase.database()
