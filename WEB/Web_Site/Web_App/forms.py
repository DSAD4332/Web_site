# forms.py
from django import forms
from .models import CustomUser, Product, Subcategory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2') # Укажите необходимые поля

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class CustomUserLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'your-checkbox-class'}))
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'your-input-class', 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'your-password-class', 'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'your-input-class'})
        self.fields['password'].widget.attrs.update({'class': 'your-password-class'})
        self.fields['remember_me'].widget.attrs.update({'class': 'your-checkbox-class'})

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'stock_quantity', 'price', 'subcategory', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
            }
    subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.all(), empty_label="Выберите подкатегорию")