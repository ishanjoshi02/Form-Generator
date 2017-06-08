from django.conf.urls import url
from . import views

app_name = 'creator'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register_user, name='register'),
    url(r'^login$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^create_form/$', views.create_form, name='create_form'),
    url(r'^(?P<form_id>[0-9]+)/delete_form/$', views.delete_form, name='delete_form'),
    url(r'^(?P<form_id>[0-9]+)/add_field/$', views.create_field, name='create_field'),
    url(r'^(?P<form_id>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^(?P<form_id>[0-9]+)/edit_form/$', views.edit_form, name='edit_form')
]