from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'input'

urlpatterns = [
    url(r'^(?P<form_id>[0-9]+)/(?P<sr_no>[0-9]+)/display_form/$',
        login_required(views.display_form, login_url='creator:login_user'), name='display_form'),
]
