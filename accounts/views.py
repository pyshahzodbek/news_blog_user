from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class LogoutPageView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')
