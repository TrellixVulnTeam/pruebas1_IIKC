from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicioSesion, name='homejvc'),
    path('dashboard/', views.dashboard, name='dashboardjvc'),
]