from django.contrib import admin
from .models import ProductoSolar

@admin.register(ProductoSolar)
class ProductoSolarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'fecha_agregado')
    search_fields = ('nombre',)
    list_filter = ('fecha_agregado',)
