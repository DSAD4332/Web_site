from django.contrib import admin
from .models import CustomUser, Product, Company, Order, OrderItem, Category, Subcategory, Review


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'address', 'role')
    search_fields = ('username', 'email')
    list_filter = ('role',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'subcategory', 'stock_quantity')
    search_fields = ('name',)
    list_filter = ('subcategory',)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'category')
    search_fields = ('name', 'email')
    list_filter = ('category',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_cost', 'status', 'order_date', 'delivery_type')
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'delivery_type')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
    search_fields = ('order__id', 'product__name')
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'company', 'rating', 'comment')
    list_filter = ('rating', 'author')
    search_fields = ('comment', 'author__username', 'product__name', 'company__name')


admin.site.register(Review, ReviewAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)