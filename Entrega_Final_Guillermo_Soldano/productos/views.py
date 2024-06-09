from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Producto
from productos.form import ProductosForm

def index(request):
    return render(request, 'productos/index.html')

def productos_list(request):
    consulta = Producto.objects.all()
    contexto = {"productos":consulta}
    return render(request,"productos/productos_list.html", contexto)

def productos_create(request):
    if request.method == "POST":
        form = ProductosForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("productos:productos_list")
    else:
        form = ProductosForm()
    return render(request, "productos/productos_form.html", {"form": form})

def productos_delete(request,pk):
    consulta = Producto.objects.get(id=pk)
    if request.method == "GET":
        consulta.delete()
        return redirect("productos:productos_list")
    return render (request, "productos/productos_delete.html",{"object":consulta})

def producto_modificar(request,pk):
    consulta = Producto.objects.get(id=pk)
    if request.method == "POST":
        form = ProductosForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("productos:productos_list")
    else:
        form = ProductosForm(instance=consulta)
    return render(request, "productos/productos_form.html", {"form": form})