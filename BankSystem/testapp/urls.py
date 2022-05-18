from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('bank', views.BankViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('jump/', views.jumpfunc),
    path('restest/', views.restest),
]
