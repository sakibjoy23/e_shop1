
# shop/urls.py

from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('products/', views.product_list, name="product_list"),  # Product listing
    path('products/<slug:slug>/', views.product_detail, name="product_detail"),  # Product detail by slug
    path('cart/', views.cart_view, name="cart"),  # View shopping cart
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name="order_confirmation"),  # Order confirmation
]