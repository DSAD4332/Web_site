# forms.py
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'address', 'role']
        widgets = {'password': forms.PasswordInput()}


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'address', 'role')  # добавьте поля, которые нужны в форме
