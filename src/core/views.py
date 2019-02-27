from django.shortcuts import render

from .models import Good
from .util import get_first_good_pic

def home_view(request):
    context = {

    }
    return render(request, 'home.html', context)


def shop_view(request):
    g_first_image = []
    goods_list = Good.objects.all()
    # get first image of all goods:
    for item in goods_list:
        g_first_image.append(get_first_good_pic(item.id))
    context = {
        'goods_list': goods_list,
        'first_image': g_first_image,
    }
    return render(request, 'shop.html', context)


def error_view(request):
    context = {

    }
    return render(request, '404.html', context)


def panel_view(request):
    context = {

    }
    return render(request, 'panel.html', context)
