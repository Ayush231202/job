from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
  path('',views.welcome, name='login'),
  path('hello', views.hello),
  path('registration',views.Register,name='signup'),
  path('forgetpass',views.forget, name='forget')
]