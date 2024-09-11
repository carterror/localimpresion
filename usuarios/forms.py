# usuarios/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ("first_name", "email", "username", "email", "password1", "password2")

class PerfilForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                 label="Nombre")
    username = forms.CharField(min_length=5,
                               widget=forms.TextInput(attrs={"class": "form-control"}),
                               label="Nombre de Usuario")
    email = forms.EmailField(disabled=True,
                             label='Correo'
                             ,widget=forms.EmailInput(attrs={"class": "form-control"}))
    class Meta:
        model = Usuario
        fields = ["first_name", "username", "email"]