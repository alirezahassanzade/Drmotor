from django.shortcuts import render


def profile_view(request):
    context = {

    }
    return render(request, 'users/profile.html', context)


def login_view(request):
    context = {

    }
    return render(request, 'users/login.html', context)


def register_view(request):
    context = {

    }
    return render(request, 'users/register.html', context)
