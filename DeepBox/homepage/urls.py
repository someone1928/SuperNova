from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.userhome,name='userhome'),
    path('profile',views.profile,name='profile'),
    path('post',views.post,name='post'),

]
