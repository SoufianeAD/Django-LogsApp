from django.urls import path
from . import views

app_name = 'application'

urlpatterns = [
    path('', views.index, name='index'),
    path('newLog/', views.newLog, name='newLog'),
    path('filter/', views.filter, name='filter'),
]

