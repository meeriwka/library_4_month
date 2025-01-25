from django.urls import path
from . import views

urlpatterns = [
    path('raritet_list/', views.RaritetListView.as_view(), name='raritet_list'),
    path('raritet_form/', views.RaritetFormView.as_view(), name='raritet_form'),
]