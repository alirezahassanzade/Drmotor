from django.shortcuts import render

from .forms import LoginForm, SignupForm
from shop.models import Good
from users.models import User

from Drmotori.util import string_to_md5


def shop_view(request):
    # '/static/img/nopic.png'
    goods_list = Good.objects.all()
    login_form = LoginForm(request.POST or None)
    signup_form = SignupForm(request.POST or None)
    context = {
        'signup_form': signup_form,
        'login_form': login_form,
        'goods_list': goods_list,
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
