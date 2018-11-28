from django.shortcuts import render
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
# from cms.core.models import User

from django.contrib.auth import logout


def user_login(request):
    form = UserLoginForm(request.POST or None)

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main'))

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')


        if username and password:
            user = authenticate(username=username, password=password)
            if user.is_authenticated:
                login(request, user)
                return HttpResponseRedirect(reverse('main'))

            else:
                messages.error(request, 'username or password is incorrect.')
                return HttpResponseRedirect(reverse('login'))


    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

