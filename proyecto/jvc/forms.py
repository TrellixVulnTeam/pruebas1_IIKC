from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from usuario.models import Usuario


class InicioSesionForm(forms.Form):
    usuario = forms.CharField(max_length=50, required=True)
    clave = forms.CharField(widget=forms.PasswordInput())
