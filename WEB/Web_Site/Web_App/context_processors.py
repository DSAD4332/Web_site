from .forms import CustomUserCreationForm, CustomUserLoginForm, ProductForm, CartItemForm

def registration_form(request):
    return {'registration_form': CustomUserCreationForm()}

def login_form(request):
    return {'login_form': CustomUserLoginForm()}

def product_form(request):
    return {'product_form': ProductForm()}

def cart_item_form(request):
    return {'cart_item_form': CartItemForm()}