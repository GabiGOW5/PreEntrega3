from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ComicForm(forms.Form):
    comic = forms.CharField(max_length=40, required= True)
    precio = forms.IntegerField(required= True)


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required= True)
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Confirma Contraseña", widget= forms.PasswordInput )