from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('',views.show_dashboard, name='show_dashboard'),
    path('add/',views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    # path('delete/', views.delete, name='delete'),
]