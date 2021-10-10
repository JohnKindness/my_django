from django.shortcuts import render
import json
# Create your views here.


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
        'products': [{'name_1': 'Худи черного цвета с монограммами adidas Originals', 'price_1': 6090},
                     {'name_2': 'Синяя куртка The North Face', 'price_2': 23725},
                     {'name_3': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price_3': 3390},
                     {'name_4': 'Черный рюкзак Nike Heritage', 'price_4': 2340},
                     {'name_5': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price_5': 13590},
                     {'name_6': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price_6': 2890},
        ]
    }
    return render(request, 'products/products.html', my_dict)
