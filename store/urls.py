"""Order_MS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('about/', views.about, name='store-about'),


    path('products/', views.ProductListView.as_view(), name='store-products'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', views.ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<id>/delete/', views.delete_product_view, name='product-delete'),


    path('orders/', views.OrderListView.as_view(), name='store-orders'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('order/new/', views.OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order-update'),
    path('order/<id>/delete/', views.delete_order_view, name='order-delete'),

    
    ]
