from django import forms
from django.contrib.auth import get_user_model




class UserForm(forms.Form):

    username=forms.CharField(max_length=20,required=True)
    password = forms.CharField(max_length=20, required=True)


class UserRegForm(UserForm):
    # username = forms.CharField(max_length=20, required=True)
    # password = forms.CharField(max_length=20, required=True)
    email=forms.EmailField(required=True)
