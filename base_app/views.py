from django.shortcuts import render, redirect
from .models import Task

from django.views.generic.list import ListView 
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

#User Registration methods
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin

#user login
class  UserLogin(LoginView):
    template_name = 'base_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


#user registration
class RegistrationPage(FormView):
    template_name = 'base_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user=True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistrationPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegistrationPage, self).get(self, *args, **kwargs)
        

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'base_app/index.html'
    context_object_name = 'list'