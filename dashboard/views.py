from cmath import log
from datetime import datetime, timedelta
from django.shortcuts import render
import pytz
from .models import Product
from django.core import serializers

def index_page(request):
    return render(request, 'index.html', {})

def products_list_page(request):
    products = Product.objects.all().order_by('-created_at')
    total = 0
    
    for product in products:
        product.images_raw = product.images.all()
        product.main_image = product.images_raw[0].image
        past = datetime.now() - timedelta(days=3)
        product_date = datetime(product.created_at.year, product.created_at.month, product.created_at.day, product.created_at.hour, product.created_at.minute)
        product.is_new = True if past < product_date else False
        total += 1

    return render(request, 'products-list.html', {
        'products': products,
        'total': total,
    })

def products_overview_page(request, id):
    product = Product.objects.get(id=id)

    product.images_raw = product.images.all()
    materials = product.material_care.split('\n')
    product.material1 = []
    product.material2 = []
    for _i, material in enumerate(materials):
        if len(materials) / 2 < _i:
            product.material2.append(material)
        else:
            product.material1.append(material)   

    product.blogs_raw = []
    blogs = product.blogs.all()
    for _i, blog in enumerate(blogs):
        if _i % 2 == 1:
            blog.is_right = True
        product.blogs_raw.append(blog)            

    return render(request, 'product.html', {
        'product': product,
    })

def cart(request):
    return render(request, 'cart.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})
