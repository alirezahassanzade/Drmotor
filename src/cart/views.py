from django.shortcuts import render


def cart_view(request):
    context = {

    }
    return render(request, 'cart/index.html', context)
