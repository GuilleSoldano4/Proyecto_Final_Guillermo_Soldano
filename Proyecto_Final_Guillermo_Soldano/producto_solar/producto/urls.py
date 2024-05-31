from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('termotanques/', views.termotanques, name='termotanques'),
    path('luminarias/', views.luminarias, name='luminarias'),
    path('otros_productos/', views.otros_productos, name='otros_productos'),
    path('contacto/', views.contacto, name='contacto'),
]
