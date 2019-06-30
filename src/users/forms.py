from django import forms
from django.contrib.auth.forms import (
    UserCreationForm as DjangoUserCreationForm
)
from django.contrib.auth.forms import UsernameField
from .models import User
import logging
from django.contrib.auth import authenticate

logger = logging.getLogger(__name__)


class UserCreationForm(DjangoUserCreationForm):

    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = ("phone_number", "first_name", "last_name",)
        field_classes = {"phone_number": UsernameField}


class AuthenticationForm(forms.Form):
    phone_number = forms.EmailField()
    password = forms.CharField(
        strip=False, widget=forms.PasswordInput
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        phone_number = self.cleaned_data.get("phone_number")
        password = self.cleaned_data.get("password")
        if phone_number is not None and password:
            self.user = authenticate(
                self.request, phone_number=phone_number, password=password
            )
            if self.user is None:
                raise forms.ValidationError(
                   "Invalid phone number/password combination."
                   )
            logger.info(
                "Authentication successful for phone_number=%s", phone_number
            )
        return self.cleaned_data

    def get_user(self):
        return self.user
