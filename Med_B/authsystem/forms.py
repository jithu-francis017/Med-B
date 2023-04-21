from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']