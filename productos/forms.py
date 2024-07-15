from django import forms
from .models import Producto, Cliente,Genero
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    pass