from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductoSolar
from .forms import ProductoSolarForm

def listar_productos(request):
    productos = ProductoSolar.objects.all()
    return render(request, 'nombre_de_tu_app1/listar_productos.html', {'productos': productos})

def detalle_producto(request, id):
    producto = get_object_or_404(ProductoSolar, id=id)
    return render(request, 'nombre_de_tu_app1/detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoSolarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoSolarForm()
    return render(request, 'nombre_de_tu_app1/crear_producto.html', {'form': form})

def editar_producto(request, id):
    producto = get_object_or_404(ProductoSolar, id=id)
    if request.method == 'POST':
        form = ProductoSolarForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoSolarForm(instance=producto)
    return render(request, 'nombre_de_tu_app1/editar_producto.html', {'form': form})

def eliminar_producto(request, id):
    producto = get_object_or_404(ProductoSolar, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'nombre_de_tu_app1/eliminar_producto.html', {'producto': producto})

def about(request):
    return render(request, 'nombre_de_tu_app1/about.html')
