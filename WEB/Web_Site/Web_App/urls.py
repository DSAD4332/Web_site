from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views
from .views import CategoryViewSet, SubcategoryViewSet, ProductViewSet, CompanyViewSet, OrderViewSet, CustomUserViewSet, ReviewViewSet

# Создание маршрутизатора и регистрация наших ViewSets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'users', CustomUserViewSet)
router.register(r'reviews', ReviewViewSet)

# Объединение URL-конфигураций
urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^home$', views.home, name='home'),
    path("projects/", views.projects, name="projects"), 
    path("contact/", views.contact, name="contact"), 
    path('', include(router.urls)), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()