from django import forms
from .models import ProductoSolar

class ProductoSolarForm(forms.ModelForm):
    class Meta:
        model = ProductoSolar
        fields = ['nombre', 'descripcion', 'precio', 'stock']
