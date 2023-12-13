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
    STOCK_STATUS_CHOICES = [
        ('in_stock', 'В наличии'),
        ('out_of_stock', 'Нет в наличии'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='product_images/')
    stock_quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, help_text="Скидка в процентах")
    stock_status = models.CharField(max_length=15, choices=STOCK_STATUS_CHOICES, default='in_stock')


    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='companies', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

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
            self.delivery_charge = 100.00
        else:
            self.delivery_charge = 0.00
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # Оценка от 1 до 5

    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, related_name='reviews', on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.author.username} on {self.product or self.company}"
    
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)