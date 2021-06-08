from django.urls import path
from . import views

urlpatterns=[
    path('',views.index1,name='index1'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('login', views.loginUser,name="login"),
    path('logout', views.logoutUser,name="logout"),

   
    


]