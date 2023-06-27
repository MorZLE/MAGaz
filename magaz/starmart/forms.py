from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class': 'form-input'}))


    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'})
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class OrderData(forms.ModelForm):
    class Meta:
        model = RecipientData
        fields = "__all__"
