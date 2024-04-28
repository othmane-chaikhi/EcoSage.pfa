from django.urls import path
from . import views 

urlpatterns =[
    path('', views.home,name='home'),
    path('/rapport', views.rapport, name='rapport'),
    path('/statistiques', views.statistiques, name='statistiques'),
   
]