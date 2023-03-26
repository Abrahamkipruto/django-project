from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('admin/', views.add, name='admin'),
  path('dashboard/', views.dash, name='dashboard'),
]