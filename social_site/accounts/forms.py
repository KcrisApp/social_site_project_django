from dataclasses import fields
# Librerie per form autenticazione
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# --------------------------------------------------------

class FormRegistrazione(UserCreationForm):

    email = forms.CharField(max_length=30,required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']