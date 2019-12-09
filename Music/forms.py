from django.contrib.auth.models import User
from django import forms
class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=200)

    class Meta:

        model = User
        fields = ['username','email','password','first_name','last_name']
