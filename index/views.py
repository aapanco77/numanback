from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, render
from django.views import generic as generic_views

class LoginView(auth_views.LoginView):
     template_name = "index/login.html"
     redirect_authenticated_user = True

