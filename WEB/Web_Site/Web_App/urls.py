# urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views
from .views import CategoryViewSet, SubcategoryViewSet, ProductViewSet, CompanyViewSet, OrderViewSet, CustomUserViewSet, ReviewViewSet, CartViewSet, registration_view

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
    re_path(r'^$', views.base, name='base'),
    re_path(r'^base$', views.base, name='base'),
    re_path(r'^products/$', views.products, name="products"), 
    re_path(r'^contact/$', views.contact, name="contact"),
    path('', include(router.urls)), 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()