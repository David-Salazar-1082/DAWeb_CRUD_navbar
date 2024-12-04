from django.shortcuts import render,redirect
from .models import Venta

# Create your views here.

def inicio_vistaVenta(request):
    lasventas=Venta.objects.all()
    return render(request, 'gestionarVentas.html', {'ventas': lasventas})


def registrarVenta(request):
    Id_Venta = request.POST['txtid']
    total = request.POST['txttotal']
    fecha = request.POST['txtfecha']
    Id_Empleado = request.POST['txtide']
    Id_Cliente = request.POST['txtidc']
    Id_Sucursal = request.POST['txtids']
    Productos_Comprados = request.POST['txtproductos_comprados']

    registrarVenta =Venta.objects.create(Id_Venta=Id_Venta, total=total, fecha=fecha, 
                                               Id_Empleado=Id_Empleado, Id_Cliente=Id_Cliente, Id_Sucursal=Id_Sucursal, Productos_Comprados=Productos_Comprados)
    return redirect('ventas')
    
def seleccionarVenta(request,Id_Venta):
    venta=Venta.objects.get(Id_Venta=Id_Venta)
    return render(request,"editarVentas.html",{"misventas":venta})

def editarVenta(request):
    Id_Venta = request.POST['txtid']
    total = request.POST['txttotal']
    fecha = request.POST['txtfecha']
    Id_Empleado = request.POST['txtide']
    Id_Cliente = request.POST['txtidc']
    Id_Sucursal = request.POST['txtids']
    Productos_Comprados = request.POST['txtproductos_comprados']
    
    venta=Venta.objects.get(Id_Venta=Id_Venta)
    venta.total = total
    venta.fecha = fecha
    venta.Id_Empleado = Id_Empleado
    venta.Id_Cliente = Id_Cliente
    venta.Id_Sucursal = Id_Sucursal
    venta.Productos_Comprados = Productos_Comprados
    venta.save()
    return redirect('ventas')

def borrarVenta(request,Id_Venta):
    venta=Venta.objects.get(Id_Venta=Id_Venta)
    venta.delete()
    return redirect('ventas')