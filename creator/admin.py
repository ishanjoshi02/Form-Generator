# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Form, TextField, NumericField, DateField, MCQField, MemoField

admin.site.register(Form)
admin.site.register(TextField)
admin.site.register(NumericField)
admin.site.register(DateField)
admin.site.register(MCQField)
admin.site.register(MemoField)
