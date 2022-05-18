from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('client/signin/', views.ClientSignin),
    path('client/signup/', views.ClientSignup)
]
