from django import forms
from .models import *
from datetime import date, datetime
from calendar import monthrange

BIRTH_YEARS = ('1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939',
               '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947',
               '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955',
               '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963',
               '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971',
               '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979',
               '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
               '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
               '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
               '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
               '2012', '2013', '2014', '2015', '2016')

MY_CHOICES = (
    ('Son', 'Son'),
    ('Daughter', 'Daughter'),
    ('Brother', 'Brother'),
    ('Sister', 'Sister'),
    ('Cousin', 'Cousin'),
    ('Grand Son', 'Grand Son'),
    ('Grand Daughter', 'Grand Daughter'),
    ('Nephew', 'Nephew'),
    ('Niece', 'Niece'),
    ('Friend', 'Friend'),
)



class AuthenticateForm(forms.Form):
    user_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'id': 'input_user_name', 'name': 'input_user_name',
               'class': "form-control", 'style': 'border:1px solid #D3D3D3'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'id': 'input_password', 'name': 'input_password',
               'class': "form-control"}))


class RegistrationForm(forms.Form):
    client_or_subuser = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=[['Client', 'Alzheimer Patient'],
                 ['Family_Friend', 'Family/Friend member']])

    relationship_to_client = forms.ChoiceField(choices=MY_CHOICES)

    user_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'id': 'input_user_name', 'name': 'input_user_name',
               'class': "form-control",
               'style': 'border:1px solid #D3D3D3; margin-left:20px'}))

    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'id': 'input_password', 'name': 'input_password',
               'class': "form-control",
               'style': 'border:1px solid #D3D3D3; margin-left:20px'}))

    firstname = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'id': 'input_firstname', 'name': 'input_firstname',
               'class': "form-control",
               'style': 'border:1px solid #D3D3D3; margin-left:20px'}))

    lastname = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'id': 'input_lastname', 'name': 'input_lastname',
               'class': "form-control",
               'style': 'border:1px solid #D3D3D3; margin-left:20px'}))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'id': 'input_email', 'name': 'input_email',
               'class': "form-control",
               'style': 'border:1px solid #D3D3D3; margin-left:20px'}))

    birthdate = forms.DateTimeField(widget=forms.SelectDateWidget(
        years=BIRTH_YEARS,
        attrs={'style': 'border:1px solid #D3D3D3; margin-top: 3px; margin-left:20px'}))

    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'input_phone_number', 'name': 'input_phone_number',
               'class': "form-control",
               'style': 'border:1px solid #D3D3D3; margin-left:20px'}))

    address = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'input_address', 'name': 'input_address',
               'class': "form-control",
               'style': 'border:1px solid #D3D3D3; margin-left:20px'}))

    profile_picture = forms.ImageField(widget=forms.FileInput(
        attrs={'align':'center', 'style': 'position:absolute; margin-left:20px'}))
