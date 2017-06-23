from time import timezone

from django.db import models
from creator.models import TextField, NumericField, DateField, MCQField, MemoField
from django.contrib.auth.models import User


class TextFieldInput(models.Model):
    parent_text_field = models.ForeignKey(TextField, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.parent_text_field.__str__() + " " + self.user.email


class NumericFieldInput(models.Model):
    parent_numeric_field = models.ForeignKey(NumericField, on_delete=models.CASCADE)
    answer = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.parent_text_field.__str__() + " " + self.user.email


class DateFieldInput(models.Model):
    parent_date_field = models.ForeignKey(DateField, on_delete=models.CASCADE)
    answer = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.parent_text_field.__str__() + " " + self.user.email


class MCQFieldInput(models.Model):
    parent_mcq_field = models.ForeignKey(MCQField, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)  # todo add choices from the parent field here
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.parent_text_field.__str__() + " " + self.user.email


class MemoFieldInput(models.Model):
    parent_memo_field = models.ForeignKey(MemoField, on_delete=models.CASCADE)
    answer = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.parent_text_field.__str__() + " " + self.user.email
