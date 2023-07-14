from django.urls import path
from . import views


urlpatterns = [
    path('', views.members, name='members'),
    path('gidaihtiyacimvar/', views.gida_ihtiyacim_var, name='gidaihtiyacimvar'),
    path('gidaihtiyaciolanlar/', views.gidaihtiyaciolanlar, name='gidaihtiyaciolanlar'),
    path('gidaihtiyacimvarform/', views.gidaihtiyacimvar, name='gidaihtiyacimvarform')
]