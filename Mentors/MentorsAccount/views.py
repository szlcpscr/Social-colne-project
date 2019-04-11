from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.


class Signup2(CreateView):
    form_class = forms.UserCreateForm2
    success_url = reverse_lazy('login')
    template_name = 'MentorsAccount/signup2.html'
