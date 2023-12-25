# urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib.auth import views as auth_views
from .views import CategoryViewSet, SubcategoryViewSet, ProductViewSet, CompanyViewSet, OrderViewSet, CustomUserViewSet, ReviewViewSet, CartViewSet

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
    re_path(r'^category/devices/$', views.cat_devices, name="Cat_Gadget_Devices"),
    re_path(r'^category/appliances/$', views.cat_appliances, name="Cat_Appliances"),
    re_path(r'^category/TAV/$', views.cat_TAV, name="Cat_TAV"),
    re_path(r'^category/computers/$', views.cat_computers, name="Cat_Computers"),
    re_path(r'^category/household/$', views.cat_household, name="Cat_Household"),
    re_path(r'^category/sports/$', views.cat_sports, name="Cat_Sports"),
    re_path(r'^category/construction/$', views.cat_construction, name="Cat_Construction"),
    re_path(r'^category/clothes/$', views.cat_clothes, name="Cat_Clothes"),
    re_path(r'^category/leisure/$', views.cat_leisure, name="Cat_Leisure"),
    re_path(r'^category/furniture/$', views.cat_furniture, name="Cat_Furniture"),
    re_path(r'^category/beauty/$', views.cat_beauty, name="Cat_Beauty"),
    re_path(r'^category/childprod/$', views.cat_childprod, name="Cat_Childprod"),
    re_path(r'^category/pharmacy/$', views.cat_pharmacy, name="Cat_Pharmacy"),
    re_path(r'^category/autoprod/$', views.cat_autoprod, name="Cat_Autoprod"),
    re_path(r'^category/gifts/$', views.cat_gifts, name="Cat_Gifts"),
    re_path(r'^category/accessories/$', views.cat_accessories, name="Cat_Accessories"),
    re_path(r'^category/jewelry/$', views.cat_jewelry, name="Cat_Jewelry"),
    re_path(r'^category/petprod/$', views.cat_petprod, name="Cat_Petprod"),
    re_path(r'^category/stationery/$', views.cat_stationery, name="Cat_Stationery"),
    re_path(r'^category/shoes/$', views.cat_shoes, name="Cat_Shoes"),
    re_path(r'^products/$', views.products, name="products"),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.custom_login, name='login'),
    path('', views.home, name='home'),
    path('', include(router.urls)), 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ]