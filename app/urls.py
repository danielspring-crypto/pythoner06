from django.urls import path 
from .import views 

urlpatterns = [
	path('', views.index, name='index'),
	path('daniel/', views.daniel, name='daniel'),
]