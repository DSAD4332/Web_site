from .forms import CustomUserCreationForm, CustomUserLoginForm

def registration_form(request):
    return {'registration_form': CustomUserCreationForm()}

def login_form(request):
    return {'login_form': CustomUserLoginForm()}