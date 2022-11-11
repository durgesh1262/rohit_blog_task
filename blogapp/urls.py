
from django.urls import path
from blogapp import views 

urlpatterns = [
   
    path('', views.adddata , name = 'addnewblog' ),
    path('table/', views.tabledata, name = 'table'),
    path('display/<slug:slug>', views.displayblog, name = 'display'),
    path('delete/<slug:slug>/', views.deleteblog, name = 'delete'),
    
]
