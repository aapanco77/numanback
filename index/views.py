from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

User = get_user_model()

def login_view(request):
     if request.user.is_authenticated:
          return redirect("music:show_songs")

     context = {}

     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(request, username=username, password=password)

          if not user:
               context["error"] = "Credenciales inválidas"
          else:
               login(request, user)
               next_url = request.GET.get("next")
               return redirect(next_url if next_url else "dashboard:show_dashboard")

     return render(request, "index/login.html", context)

def logout_view(request):
     logout(request)
     return redirect("users:login")

class LoginView(auth_views.LoginView):
     template_name = "index/login.html"
     redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
     pass