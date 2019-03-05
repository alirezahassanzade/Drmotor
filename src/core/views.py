from django.shortcuts import render

from .forms import LoginForm

from .models import Good, User
from .util import get_first_good_pic, string_to_md5


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
    login_form = LoginForm()
    context = {
        'login_form': login_form,
        'goods_list': goods_list,
        'first_image': g_first_image,
    }
    # if request.method == 'POST':
    # phone_number = request.POST.get('phone_number')
    # password = string_to_md5(request.POST.get('password'))
    # password = request.POST.get('password')
    # user = User.objects.filter(PhoneNumber=phone_number).filter(Password=password)
    # if len(user) == 1:
    #     print('I find one')
    # else:
    #     print('No one found')
    return render(request, 'shop.html', context)


def error_view(request):
    context = {

    }
    return render(request, '404.html', context)


def panel_view(request):
    context = {

    }
    return render(request, 'panel.html', context)
