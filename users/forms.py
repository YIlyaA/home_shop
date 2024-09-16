from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]

    username = forms.CharField()
    password = forms.CharField()


    # ########### THE FIRST WAY TO DO LOGINIG IN ############
    # username = forms.CharField(
    #     label = "Username",
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                                          'class': 'form-control',
    #                                                          'placeholder': 'Input your name'
    #                                                          }))
    #
    # password = forms.CharField(
    #     label = "Password",
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       'class': 'form-control',
    #                                       'placeholder': 'Input your password'
    #                                       }),)


class UserRegistrationForm(UserCreationForm):
    pass