from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import user_profile
from django import forms

class user_profile_form(forms.Form):
    username = forms.CharField()
    firstname = forms.CharField(max_length = 200)
    user_type = forms.CharField(max_length = 20)
    dob = forms.DateField()
    gender = forms.CharField(max_length = 20)
    phone = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length = 200)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)