from django.shortcuts import render
from .models import Producto

def index(request):
    return render(request, 'index.html')

def termotanques(request):
    termotanques_atmosfericos = Producto.objects.filter(categoria='Termotanque', nombre__icontains='atmosférico')
    termotanques_presurizados = Producto.objects.filter(categoria='Termotanque', nombre__icontains='presurizado')
    return render(request, 'termotanques.html', {
        'termotanques_atmosfericos': termotanques_atmosfericos,
        'termotanques_presurizados': termotanques_presurizados,
    })

def luminarias(request):
    luminarias = Producto.objects.filter(categoria='Luminaria')
    return render(request, 'luminarias.html', {'luminarias': luminarias})

def otros_productos(request):
    otros_productos = Producto.objects.filter(categoria='Otros')
    return render(request, 'otros_productos.html', {'otros_productos': otros_productos})

def contacto(request):
    return render(request, 'contacto.html')