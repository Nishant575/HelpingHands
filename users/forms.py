from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    upi_id = forms.TextInput()

    class Meta:
        model = User
        fields = ['username', 'email','UPI ID', 'password', 'Confirm Password']
