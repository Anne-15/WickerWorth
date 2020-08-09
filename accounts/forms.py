from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields =('Username', 'email', 'password1', 'password2')
