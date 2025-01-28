from django.urls import path
from . import views

urlpatterns = [
    path('create_basket/', views.create_basket_view, name='create_basket'),
    path('basket_list/', views.basket_list_view, name='basket_list'),
    path('basket_list/', views.basket_list_view, name='basket_detail'),
]