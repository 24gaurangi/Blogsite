from django.contrib import admin
from django.urls import path
from . import views

app_name = 'bloglist'

urlpatterns = [
    path('', views.blog_list, name='list'),
    path('create/', views.blog_create, name='create'),
    path('rest/', views.rest_view, name='rest'),
    path('<slug:slug>/', views.blog_details, name='detail')
]
