#from typing import Pattern
from django.urls import path
from fishfarm import views
urlpatterns = [
    path('', views.home,name='home'),
    path('contact', views.contact,name='contact'),
    path('register', views.register,name='register'),
    path('login', views.login,name='login'),
    path('myaccount', views.myaccount,name='myaccount'),
    path('pricing', views.pricing,name='pricing'),
    path('about', views.about,name='about'),
    path('team', views.team,name='team'),
    path('services', views.services,name='services'),
    path('accountbilling', views.accountbilling,name='accountbilling'),
    path('maintenance', views.maintenance,name='maintenance'),
    path('ourteam', views.ourteam,name='ourteam'),
    path('button', views.button,name='button'),
    path('form', views.form,name='form'),
    path('table', views.table,name='table'),
    path('error', views.error,name='error'),

 
]