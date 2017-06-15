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
    url(r'^(?P<form_id>[0-9]+)/(?P<field_id>[0-9]+)/delete_text_field/$', views.delete_text_field,
        name='delete_text_field'),
    url(r'^(?P<form_id>[0-9]+)/(?P<field_id>[0-9]+)/delete_numeric_field/$', views.delete_numeric_field,
        name='delete_numeric_field'),
    url(r'^(?P<form_id>[0-9]+)/(?P<field_id>[0-9]+)/delete_memo_field/$', views.delete_memo_field,
        name='delete_memo_field'),
    url(r'^(?P<form_id>[0-9]+)/(?P<field_id>[0-9]+)/delete_mcq_field/$', views.delete_mcq_field,
        name='delete_mcq_field'),
    url(r'^(?P<form_id>[0-9]+)/(?P<field_id>[0-9]+)/delete_date_field/$', views.delete_date_field,
        name='delete_date_field'),
    url(r'^(?P<form_id>[0-9]+)/add_text_field/$', views.create_text_field, name='create_text_field'),
    url(r'^(?P<form_id>[0-9]+)/add_numeric_field/$', views.create_numeric_field,
        name='create_numeric_field'),
    url(r'^(?P<form_id>[0-9]+)/add_date_field/$', views.create_date_field, name='create_date_field'),
    url(r'^(?P<form_id>[0-9]+)/add_memo_field/$', views.create_memo_field, name='create_memo_field'),
    url(r'^(?P<form_id>[0-9]+)/add_mcq_field/$', views.create_mcq_field, name='add_mcq_field'),
    url(r'^(?P<form_id>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^(?P<form_id>[0-9]+)/edit_form/$', views.edit_form, name='edit_form'),
    url(r'^(?P<field_id>[0-9]+)/edit_text_field/$', views.edit_text_field, name='edit_text_field'),
    url(r'^(?P<field_id>[0-9]+)/edit_numeric_field/$', views.edit_numeric_field, name='edit_numeric_field'),
    url(r'^(?P<field_id>[0-9]+)/edit_memo_field/$', views.edit_memo_field, name='edit_memo_field'),
    url(r'^(?P<field_id>[0-9]+)/edit_date_field/$', views.edit_date_field, name='edit_date_field'),
    url(r'^(?P<field_id>[0-9]+)/edit_mcq_field/$', views.edit_mcq_field, name='edit_mcq_field'),
]
