from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import CustomUser, Product, Order, Company, OrderItem, Category, Subcategory, Product
from .serializers import CustomUserSerializer, ProductSerializer, OrderSerializer, CompanySerializer, OrderItemSerializer, CategorySerializer, SubcategorySerializer, ProductSerializer


# Create your views here.
def home(request): 
    return render(request, "home.html")
  
def projects(request): 
    return render(request, "projects.html") 
  
def contact(request): 
    return render(request, "contact.html")

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешить удаление, если пользователь является владельцем объекта или администратором
        return obj.user == request.user or request.user.is_staff


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def list(self, request, *args, **kwargs):
        # Кастомная логика для метода GET списка пользователей
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Пример переопределения метода create
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

    # Пример переопределения метода retrieve
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
    permission_classes = [IsOwnerOrAdmin]

    # Пример переопределения метода update
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
        return Response(status=status.HTTP_204_NO_CONTENT)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        # Логика выбора категорий
        category = self.request.query_params.get('category', 'all')
        if category == 'all':
            return Company.objects.all()
        return Company.objects.filter(category=category)

    # Пример переопределения метода list
    def list(self, request, *args, **kwargs):
        # Кастомная логика для метода GET списка компаний
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Пример переопределения метода destroy
    def destroy(self, request, *args, **kwargs):
        # Кастомная логика для метода DELETE (удаление компании)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    
    # Пример переопределения метода create
    def create(self, request, *args, **kwargs):
        # Кастомная логика для метода POST (создание пункта заказа)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    # Пример переопределения метода update
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