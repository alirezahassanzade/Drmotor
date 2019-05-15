from django.shortcuts import render

from .forms import LoginForm, SignupForm, HomeRquestForm

from .models import Good, User, Request
from .util import get_first_good_pic, string_to_md5, send_mail


def home_view(request):
    request_form = HomeRquestForm(request.POST or None)
    context = {
        'request_form': request_form,
    }
    if request_form.is_valid():
        first_name = request_form.cleaned_data.get('first_name')
        last_name = request_form.cleaned_data.get('last_name')
        phone_number = request_form.cleaned_data.get('phone_number')
        description = request_form.cleaned_data.get('description')
        if first_name and last_name and phone_number and description:
            obj_request = Request()
            details = f'{first_name} {last_name}\n{phone_number}\n{description}'
            obj_request.Description = details
            send_mail(details)
            obj_request.save()
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
        password = string_to_md5(login_form.cleaned_data.get('password'))
        user = User.objects.filter(PhoneNumber=phone_number).filter(Password=password)
        if len(user) == 1:
            print('Use Successfuly logged in!')
        else:
            print('Login attemp unsuccessfuly!')
    if signup_form.is_valid():
        first_name = signup_form.cleaned_data.get('first_name')
        last_name = signup_form.cleaned_data.get('last_name')
        phone_number = signup_form.cleaned_data.get('phone_number')
        hashed_password = string_to_md5(signup_form.cleaned_data.get('password'))
        new_user = User(FirstName=first_name, LastName=last_name, PhoneNumber=phone_number, Password=hashed_password, Wallet=0)
        new_user.save()
        print('User Successfuly created !')

    return render(request, 'shop.html', context)


def error_view(request):
    context = {

    }
    return render(request, '404.html', context)


def panel_view(request):
    context = {

    }
    return render(request, 'panel.html', context)


def emergency_view(request):
    if request.method == "POST":
        print(request.POST)

    context = {

    }
    return render(request, 'emergency.html', context)
