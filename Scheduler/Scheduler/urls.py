from django.contrib import admin
from django.urls import path, include
from schedule import views

urlpatterns = [
    path('', include('schedule.urls')),
    path('home/', views.home)
]
