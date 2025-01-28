from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('fairy_tales/', views.all_products, name='fairy_tales'),
    path('fantasy/', views.all_products, name='fantasy'),
    path('drama/', views.all_products, name='drama'),

]