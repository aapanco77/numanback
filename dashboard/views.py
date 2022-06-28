from django.shortcuts import render
from django.http import HttpResponse
from .models import Team


def show_dashboard(request):
    members = Team.objects.all().values
    return render(request, 'dashboard/dashboard.html', {'members': members})