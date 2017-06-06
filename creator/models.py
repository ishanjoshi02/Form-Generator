from django.contrib.auth.models import User
from django.db import models


class Form(models.Model):
    user = models.ForeignKey(User, default=1)
    form_name = models.CharField(max_length=100, default="New Form")
    header_text = models.CharField(max_length=100)
    body_text = models.CharField(max_length=1000)
    deployed = models.BooleanField(default=False)

    # database_path = models.CharField(max_length=10000)
    # Above field may or may not be needed depending on the code used to save the data

    def __str__(self):
        return self.form_name

    def jsonToForm(self, json):
        self.form_name = json['form_name']
        self.header_text = json['header_text']
        self.body_text = json['body_text']
        self.deployed = json['deployed']


class Field(models.Model):
    caption = models.CharField(max_length=100)
    question = models.CharField(max_length=1000)
    required = models.BooleanField(default=False)
    parent_form = models.ForeignKey(Form, on_delete=models.CASCADE, default=1)

    def __str__(self):
        self.caption
