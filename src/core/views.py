from django.shortcuts import render


from .forms import HomeRquestForm
from Drmotori.util import send_mail


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


def error_view(request):
    context = {

    }
    return render(request, '404.html', context)


# def emergency_view(request):
#     if request.method == "POST":
#         # lat, lng = request.POST.get('')
#         print(request.POST)
#
#     context = {
#
#     }
#     return render(request, 'emergency.html', context)
