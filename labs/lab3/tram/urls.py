from django.urls import path
from . import views

urlpatterns = [
    path('', views.tram_net, name='home'),
    path('route/', views.find_route, name='find_route'),
    ]