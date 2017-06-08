# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Form, TextField

admin.site.register(Form)
admin.site.register(TextField)
