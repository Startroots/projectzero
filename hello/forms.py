from django.forms import fields
from django import forms
from .models import Job

class CreatejobForm(forms.ModelForm):
    class Meta:
        model= Job
        fields=[
            'company',
            'title',
            'description',
            'link',
            'link_picture',
            'category',
            'tag'
        ]
        widgets = {
            'company': forms.TextInput(attrs={'class': 'base-input-input','placeholder': 'Nombre compañia', 'autocomplete': 'off', 'autofocus': True}),
            'title': forms.TextInput(attrs={'class': 'base-input-input','placeholder': 'Titulo de la oferta', 'autocomplete': 'off', 'required': True}),
            'description': forms.TextInput(attrs={'class': 'base-input-input','placeholder': 'Descripcion', 'autocomplete': 'off', 'required': True}),
            'link': forms.TextInput(attrs={'class': 'base-input-input','placeholder': 'Link de la compañia', 'autocomplete': 'off', 'required': True}),
            'link_picture': forms.TextInput(attrs={'class': 'base-input-input','placeholder': 'link foto compañia', 'autocomplete': 'off', 'required': True}),
            'category': forms.Select(attrs={'class': 'base-input-input','placeholder': 'categoria', 'autocomplete': 'off', 'required': True}),
            'tag': forms.TextInput(attrs={'class': 'base-input-input', 'placeholder': 'Django Javascript Python', 'autocomplete': 'off', 'required': True}),
            
        }