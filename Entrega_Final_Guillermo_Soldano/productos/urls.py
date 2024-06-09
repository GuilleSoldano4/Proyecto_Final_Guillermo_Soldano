from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from productos.views import index, productos_list, productos_create,productos_delete, producto_modificar

app_name= "productos"

urlpatterns = [
    path('',index, name='index'),
    path('productos/productos_create/', productos_create, name='productos_create'),
    path('productos/productos_list/', productos_list, name='productos_list'),
    path('productos/productos_modificar/<int:pk>', producto_modificar, name='productos_modificar'),
    path('productos/productos_delete/<int:pk>/', productos_delete, name='productos_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)