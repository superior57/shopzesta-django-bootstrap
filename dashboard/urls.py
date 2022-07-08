from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('products', views.products_list_page, name='products'),
    re_path(r'products/(?P<id>[a-zA-Z0-9-]+)/$', views.products_overview_page, name='product'),

    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]
