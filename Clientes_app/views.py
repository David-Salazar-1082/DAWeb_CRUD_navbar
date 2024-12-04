from django.shortcuts import render, redirect
from .models import Clientes

# Create your views here.

def inicio_vistaClientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'gestionarClientes.html', {'clientes': clientes})

def registrarClientes(request):
    Id_Cliente =  request.POST['txtid']
    nombre =  request.POST['txtnombre']
    apellidos = request.POST['txtapellidos']
    edad = request.POST['txtedad']
    sexo = request.POST['txtsexo']
    dni = request.POST['DNI']
    fecha_nacimiento = request.POST['txtfecha']
    
    guardarC = Clientes.objects.create(Id_Cliente=Id_Cliente, nombre=nombre, apellidos=apellidos,
                                                    edad=edad, sexo=sexo, dni=dni, fecha_nacimiento=fecha_nacimiento)
    return redirect('clientes')

def seleccionarClientes( request, Id_Cliente):
    clientes = Clientes.objects.get(Id_Cliente=Id_Cliente)
    return render(request, 'editarClientes.html', {'clientes': clientes})

def editarClientes(request):
    Id_Cliente =  request.POST['txtid']
    nombre =  request.POST['txtnombre']
    apellidos = request.POST['txtapellidos']
    edad = request.POST['txtedad']
    sexo = request.POST['txtsexo']
    dni = request.POST['DNI']
    fecha_nacimiento = request.POST['txtfecha']
    
    clientes = Clientes.objects.get(Id_Cliente=Id_Cliente)
    clientes.nombre = nombre
    clientes.apellidos = apellidos
    clientes.edad = edad
    clientes.sexo = sexo
    clientes.dni = dni
    clientes.fecha_nacimiento = fecha_nacimiento 
    clientes.save()
    return redirect('clientes')

def borrarClientes(request,Id_Cliente):
    clientes=Clientes.objects.get(Id_Cliente=Id_Cliente)
    clientes.delete()
    return redirect("clientes")