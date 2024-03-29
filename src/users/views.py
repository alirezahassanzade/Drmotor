from django.shortcuts import render
import logging
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from .forms import UserCreationForm, AuthenticationForm


logger = logging.getLogger(__name__)

BASE_URL = getattr(settings, 'BASE_URL', 'https://www.pedram-parsian.com')
DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)


class SignupView(FormView):
    template_name = "users/signup.html"
    form_class = UserCreationForm

    def get_success_url(self):
        redirect_to = self.request.GET.get("next", "/")
        return redirect_to

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()

        phone_number = form.cleaned_data.get("phone_number")
        raw_password = form.cleaned_data.get("password1")
        logger.info(
            "New signup for phone_number=%s through SignupView", phone_number
        )

        user = authenticate(phone_number=phone_number, password=raw_password)
        login(self.request, user)

        messages.info(
            self.request, "You signed up successfully."
        )

        return response


def profile_view(request):
    context = {

    }
    return render(request, 'users/profile.html', context)


class SignoutView(LogoutView):
    template_name = "users/signout.html"

    def get_next_url(self):
        redirect_to = self.request.GET.get("next", "/")
        return redirect_to


class SigninView(LoginView):
    template_name = 'users/signin.html'
    form_class = AuthenticationForm
