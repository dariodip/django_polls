from django import forms
from django.forms import widgets
from django.core.validators import validate_email


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=3, required=True)
    first_name = forms.CharField(min_length=3, max_length=30, required=True)
    last_name = forms.CharField(min_length=3, max_length=30, required=True)
    email = forms.CharField(min_length=3, max_length=50, required=True, validators=[validate_email])
    password = forms.CharField(widget=widgets.PasswordInput(), required=True, min_length=5, max_length=32)
