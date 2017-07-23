from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'creator'

urlpatterns = [
    url(r'^$', login_required(views.index, login_url='creator:login_user'), name='index'),
    url(r'^register$', views.register_user, name='register'),
    url(r'^login$', views.login_user, name='login_user'),
    url(r'^logout_user/$', login_required(views.logout_user, login_url='creator:login_user'), name='logout_user'),
    url(r'^create_form/$', login_required(views.create_form, login_url='creator:login_user'), name='create_form'),
    url(r'^(?P<form_id>[0-9]+)/results/$', login_required(views.result, login_url='creator:login_user'), name='result'),
    url(r'^(?P<form_id>[0-9]+)/delete_form/$', login_required(views.delete_form, login_url='creator:login_user'), name='delete_form'),
    url(r'^(?P<form_id>[0-9]+)/(?P<field_id>[0-9]+)/delete_text_field/$',
        login_required(views.delete_text_field, login_url='creator:login_user'), name='delete_text_field'),
    url(r'^(?P<form_id>[0-9]+)/(?P<field_id>[0-9]+)/delete_numeric_field/$',
        login_required(views.delete_numeric_field, login_url='creator:login_user'), name='delete_numeric_field'),
    url(r'^(?P<form_id>[0-9]+)/(?P<field_id>[0-9]+)/delete_memo_field/$',
        login_required(views.delete_memo_field, login_url='creator:login_user'), name='delete_memo_field'),
    url(r'^(?P<form_id>[0-9]+)/(?P<field_id>[0-9]+)/delete_mcq_field/$',
        login_required(views.delete_mcq_field, login_url='creator:login_user'), name='delete_mcq_field'),
    url(r'^(?P<form_id>[0-9]+)/(?P<field_id>[0-9]+)/delete_date_field/$',
        login_required(views.delete_date_field, login_url='creator:login_user'), name='delete_date_field'),
    url(r'^(?P<form_id>[0-9]+)/add_text_field/$',
        login_required(views.create_text_field, login_url='creator:login_user'), name='create_text_field'),
    url(r'^(?P<form_id>[0-9]+)/add_numeric_field/$',
        login_required(views.create_numeric_field, login_url='creator:login_user'), name='create_numeric_field'),
    url(r'^(?P<form_id>[0-9]+)/add_date_field/$',
        login_required(views.create_date_field, login_url='creator:login_user'), name='create_date_field'),
    url(r'^(?P<form_id>[0-9]+)/add_memo_field/$',
        login_required(views.create_memo_field, login_url='creator:login_user'), name='create_memo_field'),
    url(r'^(?P<form_id>[0-9]+)/add_mcq_field/$',
        login_required(views.create_mcq_field, login_url='creator:login_user'), name='add_mcq_field'),
    url(r'^(?P<form_id>[0-9]+)/detail/$',
        login_required(views.detail, login_url='creator:login_user'), name='detail'),
    url(r'^(?P<form_id>[0-9]+)/edit_form/$',
        login_required(views.edit_form, login_url='creator:login_user'), name='edit_form'),
    url(r'^(?P<field_id>[0-9]+)/edit_text_field/$',
        login_required(views.edit_text_field, login_url='creator:login_user'), name='edit_text_field'),
    url(r'^(?P<field_id>[0-9]+)/edit_numeric_field/$',
        login_required(views.edit_numeric_field, login_url='creator:login_user'), name='edit_numeric_field'),
    url(r'^(?P<field_id>[0-9]+)/edit_memo_field/$',
        login_required(views.edit_memo_field, login_url='creator:login_user'), name='edit_memo_field'),
    url(r'^(?P<field_id>[0-9]+)/edit_date_field/$',
        login_required(views.edit_date_field, login_url='creator:login_user'), name='edit_date_field'),
    url(r'^(?P<field_id>[0-9]+)/edit_mcq_field/$',
        login_required(views.edit_mcq_field, login_url='creator:login_user'), name='edit_mcq_field'),
    url(r'^(?P<field_id>[0-9]+)/text_field_result/$',
        login_required(views.textFieldResult, login_url='creator:login_user'), name='text_field_result'),
    url(r'^(?P<field_id>[0-9]+)/numeric_field_result/$',
        login_required(views.numericFieldResult, login_url='creator:login_user'), name='numeric_field_result'),
    url(r'^(?P<field_id>[0-9]+)/date_field_result/$',
        login_required(views.dateFieldResult, login_url='creator:login_user'), name='date_field_result'),
    url(r'^(?P<field_id>[0-9]+)/memo_field_result/$',
        login_required(views.memoFieldResult, login_url='creator:login_user'), name='memo_field_result'),
    url(r'^(?P<field_id>[0-9]+)/mcq_field_result/$',
        login_required(views.mcqFieldResult, login_url='creator:login_user'), name='mcq_field_result'),
]
