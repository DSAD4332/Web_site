# forms.py
from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'address', 'role']
        widgets = {'password': forms.PasswordInput()}