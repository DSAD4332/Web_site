# views

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import CustomUser, Product, Order, Company, OrderItem, Category, Subcategory, Product, Review, Cart
from .serializers import CustomUserSerializer, ProductSerializer, OrderSerializer, CompanySerializer, OrderItemSerializer, CategorySerializer, SubcategorySerializer, ProductSerializer, ReviewSerializer, CartSerializer
from .permissions import IsAdminUser, IsCustomerUser, IsCourierUser, IsCompanyUser
from .forms import CustomUserCreationForm, CustomUserLoginForm, ProductForm
from django.http import JsonResponse
from django.template.loader import render_to_string

def home(request): 
    return render(request, "Home.html")
  
def contacts(request): 
    return render(request, "Contacts.html")

def checkout(request): 
    return render(request, "Checkout.html")

def cooperation(request): 
    return render(request, "Cooperation.html")

def order_confirmation(request): 
    return render(request, "Order_confirmation.html")

def products(request): 
    return render(request, "Products.html")

def catalog(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'all'}
    return render(request, "Catalog.html", ctx) 

def cat_devices(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'devices'}
    return render(request, "Cat_Gadget_Devices.html", ctx)

def cat_appliances(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'appliances'}
    return render(request, "Cat_Appliances.html", ctx)

def cat_TAV(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'TAV'}
    return render(request, "Cat_TAV.html", ctx)

def cat_computers(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'computers'}
    return render(request, "Cat_Computers.html", ctx)

def cat_household(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'household'}
    return render(request, "Cat_Household.html", ctx)

def cat_sports(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'sports'}
    return render(request, "Cat_Sports.html", ctx)

def cat_construction(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'construction'}
    return render(request, "Cat_Construction.html", ctx)

def cat_clothes(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'clothes'}
    return render(request, "Cat_Clothes.html", ctx)

def cat_leisure(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'leisure'}
    return render(request, "Cat_Leisure.html", ctx)

def cat_furniture(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'furniture'}
    return render(request, "Cat_Furniture.html", ctx)

def cat_beauty(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'beauty'}
    return render(request, "Cat_Beauty.html", ctx)

def cat_childprod(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'childprod'}
    return render(request, "Cat_Childprod.html", ctx)

def cat_pharmacy(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'pharmacy'}
    return render(request, "Cat_Pharmacy.html", ctx)

def cat_autoprod(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'autoprod'}
    return render(request, "Cat_Autoprod.html", ctx)

def cat_gifts(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'gifts'}
    return render(request, "Cat_Gifts.html", ctx)

def cat_accessories(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'accessories'}
    return render(request, "Cat_Accessories.html", ctx)

def cat_jewelry(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'jewelry'}
    return render(request, "Cat_Jewelry.html", ctx)

def cat_petprod(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'petprod'}
    return render(request, "Cat_Petprod.html", ctx)

def cat_stationery(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'stationery'}
    return render(request, "Cat_Stationery.html", ctx)

def cat_shoes(request): 
    products = Product.objects.all()
    ctx = {'products': products, 'active': 'shoes'}
    return render(request, "Cat_Shoes.html", ctx)





class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        # Кастомная логика для метода GET списка пользователей
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # Кастомная логика для метода POST (создание пользователя)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        # Кастомная логика для метода DELETE (удаление пользователя)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser | IsCustomerUser]
    

    def retrieve(self, request, *args, **kwargs):
        # Кастомная логика для метода GET одного продукта
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.query_params.get('category_id', None)
        subcategory_id = self.request.query_params.get('subcategory_id', None)

        if category_id:
            queryset = queryset.filter(subcategory__category_id=category_id)
        if subcategory_id:
            queryset = queryset.filter(subcategory_id=subcategory_id)
        return queryset

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser | IsCourierUser]

    def update(self, request, *args, **kwargs):
        # Кастомная логика для метода PUT (обновление заказа)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        order = serializer.save()
        order.update_delivery_charge()
        
    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        order.soft_delete()  # Мягкое удаление вместо физического
        order.soft_delete()  # Мягкое удаление вместо физического
        return Response(status=status.HTTP_204_NO_CONTENT)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAdminUser | IsCompanyUser]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        # Логика выбора категорий
        category = self.request.query_params.get('category', 'all')
        if category == 'all':
            return Company.objects.all()
        return Company.objects.filter(category=category)

    def list(self, request, *args, **kwargs):
        # Кастомная логика для метода GET списка компаний
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        # Кастомная логика для метода DELETE (удаление компании)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    
    def create(self, request, *args, **kwargs):
        # Кастомная логика для метода POST (создание пункта заказа)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # Кастомная логика для метода PUT (обновление пункта заказа)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_queryset(self):
        # Возвращает только неудаленные заказы
        return Order.objects.filter(is_deleted=False)
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsCustomerUser]  

    @action(detail=True, methods=['post'])
    def add_item(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        # Добавление товара в корзину...
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def remove_item(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        # Удаление товара из корзины...
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def update_quantity(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        # Изменение количества товара...
        return Response(status=status.HTTP_200_OK)
    
def list_orders(request):
    # Используем select_related для ForeignKey и prefetch_related для ManyToManyField
    orders = Order.objects.select_related('user').prefetch_related('products')
    return render(request, '/Users/tair/Documents/Колледж/Python/VS/Trading_platform/Web_site/WEB/Web_Site/Web_App/Web_AppTemps/orders/list.html', {'orders': orders})

def list_products(request):
    # Используем prefetch_related для доступа к категориям через подкатегории
    products = Product.objects.prefetch_related('subcategory__category')
    return render(request, '/Users/tair/Documents/Колледж/Python/VS/Trading_platform/Web_site/WEB/Web_Site/Web_App/Web_AppTemps/products/list.html', {'products': products})
    return render(request, '/Users/tair/Documents/Колледж/Python/VS/Trading_platform/Web_site/WEB/Web_Site/Web_App/Web_AppTemps/products/list.html', {'products': products})

def list_companies(request):
    companies = Company.objects.select_related('category')
    return render(request, '/Users/tair/Documents/Колледж/Python/VS/Trading_platform/Web_site/WEB/Web_Site/Web_App/Web_AppTemps/companies/list.html', {'companies': companies})
    return render(request, '/Users/tair/Documents/Колледж/Python/VS/Trading_platform/Web_site/WEB/Web_Site/Web_App/Web_AppTemps/companies/list.html', {'companies': companies})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Перенаправление после успешной регистрации
            redirect(request.META.get('HTTP_REFERER', 'home'))
        else:
            # Возврат к форме с отображением ошибок
            return render(request, 'Navbar.html', {'registration_form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'Navbar.html', {'registration_form': form})


def custom_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me') 
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(1209600) # 2 недели
                else:
                    request.session.set_expiry(0) 

                redirect(request.META.get('HTTP_REFERER', 'home'))
    else:
        form = CustomUserLoginForm()

    return render(request, 'Navbar.html', {'login_form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # обработка и сохранение данных формы
            return redirect('Product')
    else:
        form = ProductForm()

    return render(request, 'Product.html', {'product_form': form})