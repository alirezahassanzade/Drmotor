from django.shortcuts import render

from .models import Good


def home_view(request):
    context = {

    }
    return render(request, 'home.html', context)


def shop_view(request):
    goods_list = Good.objects.all()
    context = {
        'goods_list': goods_list
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
