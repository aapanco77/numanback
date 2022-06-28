from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Team


def show_dashboard(request):
    members = Team.objects.all().values
    return render(request, 'dashboard/dashboard.html', {'members': members})

def add(request):
    return render(request, 'dashboard/add.html')

def addrecord(request):
    companyName = request.POST['company']
    progress = request.POST['progress']
    linkCompany = request.POST['url_drive']
    dummie = request.POST['dummies']
    cowork = request.POST['coworker']
    statusCoworker = request.POST['status']
    coworkerProject = request.POST['assign_project']
    project = Team(company=companyName, progress=progress, url_drive= linkCompany, dummies=dummie, coworker=cowork, status=statusCoworker, assign_project=coworkerProject )
    project.save()
    return HttpResponseRedirect(reverse('dashboard:show_dashboard'))

# def delete(request):
#     erase = Team.objects.get
#     erase.delete()
#     return HttpResponseRedirect(reverse('dashboard:show_dashboard'))