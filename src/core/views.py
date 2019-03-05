from django.shortcuts import render

from .forms import LoginForm, SignupForm

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
    login_form = LoginForm(request.POST or None)
    signup_form = SignupForm(request.POST or None)
    context = {
        'signup_form': signup_form,
        'login_form': login_form,
        'goods_list': goods_list,
        'first_image': g_first_image,
    }
    if login_form.is_valid():
        phone_number = login_form.cleaned_data.get('phone_number')
        password = login_form.cleaned_data.get('password') #string_to_md5(login_form.cleaned_data.get('password'))
        user = User.objects.filter(PhoneNumber=phone_number).filter(Password=password)
        if len(user) == 1:
            print('I find one')
        else:
            print('No one found')
    if signup_form.is_valid():
        first_name = signup_form.cleaned_data.get('first_name')
        last_name = signup_form.cleaned_data.get('last_name')
        phone_number = signup_form.cleaned_data.get('phone_number')
        password = signup_form.cleaned_data.get('password')
        hashed_password = string_to_md5(password)
        new_user = User()

    return render(request, 'shop.html', context)


def error_view(request):
    context = {

    }
    return render(request, '404.html', context)


def panel_view(request):
    context = {

    }
    return render(request, 'panel.html', context)
