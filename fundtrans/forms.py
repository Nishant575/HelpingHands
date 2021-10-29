from django import forms
from django.contrib.auth.models import User
from .models import Transaction


class Transform():
    amount = forms.IntegerField(required=True)

    class Meta:
        model = Transaction
        fields = ['amount']
