from django.urls import path

from . import views

# app_name = 'imganalyzer'

urlpatterns = [
    path('home', views.home, name='home'),
    path('result', views.result, name='result'),
    path('details', views.details, name='details'),
]