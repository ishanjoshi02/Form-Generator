# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import TextFieldInput, NumericFieldInput, DateFieldInput, MCQFieldInput, MemoFieldInput

admin.site.register(TextFieldInput)
admin.site.register(NumericFieldInput)
admin.site.register(DateFieldInput)
admin.site.register(MCQFieldInput)
admin.site.register(MemoFieldInput)
