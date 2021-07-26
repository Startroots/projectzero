from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'base-input-input','placeholder': 'Clave', 'autocomplete': 'off', 'required': True}),
    )
    password2 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'base-input-input','placeholder': 'Confirme su clave', 'autocomplete': 'off', 'required': True}),
    )
    class Meta:
        model= User
        fields=[
            'username',
            'email',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'base-input-input','placeholder': 'Nombre Usuario', 'autocomplete': 'off', 'autofocus': True}),
            'email': forms.EmailInput(attrs={'class': 'base-input-input','placeholder': 'Correo', 'autocomplete': 'off', 'required': True}),
        }

