# urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CategoryViewSet, SubcategoryViewSet, ProductViewSet, CompanyViewSet, OrderViewSet, CustomUserViewSet, ReviewViewSet, CartViewSet, add_product

# Создание маршрутизатора и регистрация наших ViewSets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'users', CustomUserViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'carts', CartViewSet)

# Объединение URL-конфигураций
urlpatterns = [
    path('catalog', views.catalog, name="catalog"),
    path('cooperation', views.cooperation, name="cooperation"),
    path('contacts', views.contacts, name="contacts"),
    path('checkout', views.checkout, name="checkout"),
    path('order_confirmation', views.order_confirmation, name="order_confirmation"),
    path('products', views.products, name="products"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.custom_login, name='login'),
    path('producs/', views.add_product, name='products'),
    path('get-subcategories/<int:category_id>/', views.get_subcategories, name='get_subcategories'),
    path('get-products/<int:subcategory_id>/', views.get_products, name='get_products'),
    path('catalog/products/', views.product_list, name='product_list'),
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('', include(router.urls)), 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ]