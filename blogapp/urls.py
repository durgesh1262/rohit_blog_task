
from django.urls import path
from . import views 

urlpatterns = [
   
    path('add/', views.adddata , name = 'addnewblog' ),
    path('display/<slug:slug>/', views.displayblog, name = 'display'),
    path('delete/<slug:slug>/', views.deleteblog, name = 'delete'),
    
]