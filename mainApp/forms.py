from django import forms
from .models import *
from datetime import date, datetime
from calendar import monthrange


class AuthenticateForm(forms.Form):
    user_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'id': 'input_user_name', 'name': 'input_user_name',
               'class': "form-control", 'style': 'border:1px solid #D3D3D3'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'id': 'input_password', 'name': 'input_password',
               'class': "form-control"}))


class RegistrationForm(forms.Form):
    user_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'id': 'input_user_name', 'name': 'input_user_name',
               'class': "form-control"}))

    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'id': 'input_password', 'name': 'input_password',
               'class': "form-control"}))

    firstname = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'id': 'input_firstname', 'name': 'input_firstname',
               'class': "form-control", 'style': 'border:1px solid #D3D3D3'}))

    lastname = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'id': 'input_lastname', 'name': 'input_lastname',
               'class': "form-control", 'style': 'border:1px solid #D3D3D3'}))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'id': 'input_email', 'name': 'input_email',
               'class': "form-control", 'style': 'border:1px solid #D3D3D3'}))

    birthdate = forms.DateTimeField(widget=forms.DateInput(
        attrs={'id': 'input_lastname', 'name': 'input_lastname',
               'class': "form-control", 'style': 'border:1px solid #D3D3D3'}))

    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'input_phone_number', 'name': 'input_phone_number',
               'class': "form-control", 'style': 'border:1px solid #D3D3D3'}))

    address = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'input_address', 'name': 'input_address',
               'class': "form-control", 'style': 'border:1px solid #D3D3D3'}))

    profile_picture = forms.ImageField()

    about_me = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'input_about_me', 'name': 'input_about_me',
               'class': "form-control", 'style': 'border:1px solid #D3D3D3'}))
