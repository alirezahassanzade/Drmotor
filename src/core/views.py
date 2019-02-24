from django.shortcuts import render


def home_view(request):
    context = {

    }
    return render(request, 'home.html', context)


def shop_view(request):
    context = {

    }
    return render(request, 'shop.html', context)
