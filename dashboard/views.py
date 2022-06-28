from django.shortcuts import render
from django.http import HttpResponse


def show_dashboard(request):
    return render(request, 'dashboard/dashboard.html')