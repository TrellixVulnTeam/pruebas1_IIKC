from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homejvc'),
    path('dashboard/', views.dashboard, name='dashboardjvc'),
]