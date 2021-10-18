from django.shortcuts import render
from products.models import ProductCategory, Product



def index(request):
    my_dict = {
        'menu_button': 'GeekShop',
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', my_dict)


def products(request):
    my_dict = {
        'title': 'GeekShop - Каталог',
        'menu_button': 'GeekShops',
        'products': Product.objects.all(),
        'category': Product.objects.all()
    }
    return render(request, 'products/products.html', my_dict)
