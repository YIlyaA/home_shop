from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class UserLoginForm(AuthenticationForm):

    ############ THE FIRST WAY TO DO LOGINIG IN ############
    # username = forms.CharField(
    #     label = "Username",
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                                          'class': 'form-control',
    #                                                          'placeholder': 'Input your name'
    #                                                          }))

    # password = forms.CharField(
    #     label = "Password",
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       'class': 'form-control',
    #                                       'placeholder': 'Input your password'
    #                                       }),)


    ############ THE SECOND WAY TO DO LOGINIG IN ############
    username = forms.CharField()
    password = forms.CharField()


    class Meta:
        model = User
        fields = ["username", "password"]
