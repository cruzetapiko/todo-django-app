from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',UserLogin.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegistrationPage.as_view() ,name='register'),

    path('', TaskList.as_view(), name='index'),
]