from django.shortcuts import render,redirect
from .models import Producto

# Create your views here.

def inicio_vistaProducto(request):
    losproductos=Producto.objects.all()
    return render(request, 'gestionarProducto.html', {'productos': losproductos})


def registrarProducto(request):
    Id_Producto = request.POST['txtid']
    nombre = request.POST['txtnombre']
    marca = request.POST['txtmarca']
    precio = request.POST['txtprecio']
    cantidad = request.POST['txtcantidad']
    proovedor = request.POST['txtproovedor']
    categoria = request.POST['txtcategoria']

    registrarProducto =Producto.objects.create(Id_Producto=Id_Producto, nombre=nombre, marca=marca, 
                                               precio=precio, cantidad=cantidad, proovedor=proovedor, categoria=categoria)
    return redirect('productos')
    
def seleccionarProducto(request,Id_Producto):
    producto=Producto.objects.get(Id_Producto=Id_Producto)
    return render(request,"editarproducto.html",{"misproductos":producto})

def editarProducto(request):
    Id_Producto = request.POST['txtid']
    nombre = request.POST['txtnombre']
    marca = request.POST['txtmarca']
    precio = request.POST['txtprecio']
    cantidad = request.POST['txtcantidad']
    proovedor = request.POST['txtproovedor']
    categoria = request.POST['txtcategoria']
    
    producto=Producto.objects.get(Id_Producto=Id_Producto)
    producto.nombre = nombre
    producto.marca = marca
    producto.precio = precio
    producto.cantidad = cantidad
    producto.proovedor = proovedor
    producto.categoria = categoria
    producto.save()
    return redirect('productos')

def borrarProducto(request,Id_Producto):
    producto=Producto.objects.get(Id_Producto=Id_Producto)
    producto.delete()
    return redirect('productos')