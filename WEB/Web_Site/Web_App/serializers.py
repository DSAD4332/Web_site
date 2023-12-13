from rest_framework import serializers
from .models import CustomUser, Product, Company, Order, OrderItem, Category, Subcategory, Product, Review, CartItem, Cart

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'address', 'role']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'image', 'stock_quantity']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'address', 'email', 'password', 'category']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_items', 'total_cost', 'status', 'order_date', 'delivery_info', 'delivery_type', 'delivery_charge']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'category', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    subcategory_name = serializers.CharField(write_only=True, required=False)
    subcategory_details = SubcategorySerializer(source='subcategory', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'subcategory', 'subcategory_details']

    def create(self, validated_data):
        subcategory_name = validated_data.pop('subcategory_name', None)
        if subcategory_name:
            subcategory, created = Subcategory.objects.get_or_create(name=subcategory_name)
            validated_data['subcategory'] = subcategory
        return super().create(validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Review
        fields = ['id', 'product', 'company', 'author', 'author_username', 'rating', 'comment']
        
class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity']
        
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']
