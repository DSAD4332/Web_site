"""Web_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
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
    path('', include(router.urls)),  # Добавление маршрутизатора REST framework
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()