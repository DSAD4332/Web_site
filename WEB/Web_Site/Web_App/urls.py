from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import CategoryViewSet, SubcategoryViewSet, ProductViewSet, CompanyViewSet, OrderViewSet, CustomUserViewSet

# Создание маршрутизатора и регистрация наших ViewSets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'users', CustomUserViewSet)

# Объединение URL-конфигураций
urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.projects, name="projects"), 
    path("contact/", views.contact, name="contact"), 
]
urlpatterns += staticfiles_urlpatterns()