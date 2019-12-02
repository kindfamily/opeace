import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]