from django import forms
from .models import *


class SignupForm(forms.ModelForm):
    class Meta:
        model = singup
        fields = ["email", "password", "first_name"]
        labels = {
            "email": "Enter email",
            "password": "Enter Password",
            "first_name": "Enter first name",
        }
        # error_messages = {'email':{'required':'Enter email input'},'password':{'required':'Enter password input'}}
