from django.shortcuts import render
from .forms import UserLoginForm, SignupForm
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


def registerUser(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            country = form.cleaned_data.get('country')
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(password)
                user.first_name=first_name
                user.last_name=last_name
                user.save()
                user.profile.country=country
                user.profile.save()
                messages.success(request, 'User Registration succesfull!')
                return HttpResponseRedirect(reverse('register'))
        else:
            messages.success(request, 'There was an error!')
            return HttpResponseRedirect(reverse('register'))


    form = SignupForm(None)
    return render(request, 'registration/signup.html', {'form': form})


