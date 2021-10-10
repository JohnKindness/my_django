from django.shortcuts import render

# Create your views here.


def index(request):
    my_dict = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', my_dict)


def products(request):
    my_dict = {
        'title': 'GeekShop - Каталог'
    }
    return render(request, 'products/products.html', my_dict)
