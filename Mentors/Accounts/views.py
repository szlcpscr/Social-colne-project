from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import Http404
from pip._internal.cli.cmdoptions import editable
from requests import request

from . import forms

# Create your views here.


class SignUP(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'Accounts/signup.html'


class SignUp2(CreateView):
    form_class = forms.UserCreateForm2
    success_url = reverse_lazy('login2')
    template_name = 'Accounts/signup2.html'


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'Accounts/profile.html', args)


def edit_profile(requset):

    if requset.method == 'POST':
        form = forms.EditProfileForm(requset.POST, instance=requset.user)

        if form.is_valid():
            form.save()
            return redirect('/Accounts/profile')

    else:
        form = forms.EditProfileForm()
        args = {'form': form}
        return render(requset, 'Accounts/edit_profile.html', args)


def change_password(requset):

    if requset.method == 'POST':
        form = PasswordChangeForm(data=requset.POST, instance=requset.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(requset, form.user)
            return redirect('/Accounts/profile')

        else:
            return redirect('/Accounts/change-password')

    else:
        form = PasswordChangeForm(user=requset.user)
        args = {'form': form}
        return render(requset, 'Accounts/password_change.html', args)
