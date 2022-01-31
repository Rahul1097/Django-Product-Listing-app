from django.contrib import admin
from django.urls import path
from table import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('update/', views.update_data, name='update_records')
]