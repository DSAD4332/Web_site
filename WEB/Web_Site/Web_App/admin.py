from django.contrib import admin

from .models import CustomUser, Product, Company, Order, OrderItem
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Order)
admin.site.register(OrderItem)