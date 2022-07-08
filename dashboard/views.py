from django.shortcuts import render


def index_page(request):
    return render(request, 'index.html', {})


def products_list_page(request):
    return render(request, 'products-list.html', {})


def products_overview_page(request, id):
    return render(request, 'product.html', {})

def cart(request):
    return render(request, 'cart.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})
