# usuarios/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ("first_name", "email", "username", "email", "password1", "password2", "ci")
