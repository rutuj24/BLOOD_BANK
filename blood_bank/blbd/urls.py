
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('receivers', views.receivers, name='receivers'),
    path('donors', views.donors, name='donors'),
    path('workers', views.workers, name='workers'),
    path('stock', views.stock, name='stock'),
    path('myths', views.myths, name='myths'),
    path('who', views.who, name='who'),

]