from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
    path('productos/<int:id>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('about/', views.about, name='about'),
]
