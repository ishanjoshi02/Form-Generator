from django.conf.urls import url
from . import views

app_name = 'input'

urlpatterns = [
    url(r'^(?P<form_id>[0-9]+)/(?P<sr_no>[0-9]+)/display_form/$', views.display_form, name='display_form'),
]
