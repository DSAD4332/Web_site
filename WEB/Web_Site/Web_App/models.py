from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=[('customer', 'Customer'), ('admin', 'Admin'), ('company', 'Company')])

    class Meta:
        db_table = 'custom_user'


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='product_images/')
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Company(models.Model):
    CATEGORY_CHOICES = [
        ('all', 'Все'),
        ('food and drinks', 'Еда и Напитки'),
        ('beauty and health', 'Красота и Здоровье'),
        ('house and garden', 'Дом и Сад'),
        ('sports', 'Спорт'),
        ('clothing and accessories', 'Одежда и Аксессуары'),
        ('electronics and engineering', 'Электроника и Техника'),
        ('books, toys and hobbies', 'Книги, Игрушки и Хобби'),
        ('pets', 'Питомцы'),
        ('cars and transport', 'Авто и Транспорт'),
        ('floristry and gifts', 'Флористика и Подарки'),
        ('office supplies', 'Канцелярские Товары'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='companies', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='all')

class Order(models.Model):
    user = models.ForeignKey(CustomUser, related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_info = models.TextField()
    DELIVERY_CHOICES = [
        ('pickup', 'Pickup'),  # Самовывоз
        ('delivery', 'Delivery'),  # Доставка на дом
    ]
    delivery_type = models.CharField(max_length=10, choices=DELIVERY_CHOICES, default='pickup')
    delivery_charge = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    is_deleted = models.BooleanField(default=False)
    
    def soft_delete(self):
        self.is_deleted = True
        self.save()

    # Метод для обновления наценки на доставку
    def update_delivery_charge(self):
        if self.delivery_type == 'delivery':
            # Устанавливаем наценку, например, 100
            self.delivery_charge = 100.00
        else:
            self.delivery_charge = 0.00
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
