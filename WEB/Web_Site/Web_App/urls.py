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
    re_path(r'^$', views.home, name='home'),
    re_path(r'^home$', views.home, name='home'),
    re_path(r'^catalog/$', views.catalog, name="catalog"),
    re_path(r'^cooperation/$', views.cooperation, name="cooperation"),
    re_path(r'^contacts/$', views.contacts, name="contacts"),
  # re_path(r'^register/$', views.registration_view, name='register'),
    re_path(r'^checkout/$', views.checkout, name="checkout"),
    re_path(r'^order_confirmation/$', views.order_confirmation, name="order_confirmation"),
    re_path(r'^categories_stuffedAnimals/$', views.categories_stuffedAnimals, name="categories_stuffedAnimals"),
    re_path(r'^teddybear/$', views.teddybear, name="teddybear"),
    re_path(r'^products/$', views.products, name="products"),
    path('', include(router.urls)), 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ]