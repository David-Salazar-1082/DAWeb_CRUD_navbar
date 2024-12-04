from django.shortcuts import render, redirect
from .models import Empleados

# Create your views here.

def inicio_vistaEmpleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'gestionarEmpleados.html', {'empleados': empleados})

def registrarEmpleados(request):
    Id_Empleado =  request.POST['txtid']
    nombre =  request.POST['txtnombre']
    apellidos = request.POST['txtapellidos']
    sexo = request.POST['txtsexo']
    direccion = request.POST['txtsireccion']
    celular = request.POST['txtcelular']
    email = request.POST['email']
     
    guardarE = Empleados.objects.create(Id_Empleado=Id_Empleado, nombre=nombre, apellidos=apellidos,
                                                    sexo=sexo, direccion=direccion, celular=celular, email=email)
    return redirect('empleados')

def seleccionarEmpleados( request, Id_Empleado):
    empleados = Empleados.objects.get(Id_Empleado=Id_Empleado)
    return render(request, 'editarEmpleados.html', {'empleados': empleados})

def editarEmpleados(request):
    Id_Empleado =  request.POST['txtid']
    nombre =  request.POST['txtnombre']
    apellidos = request.POST['txtapellidos']
    sexo = request.POST['txtsexo']
    direccion = request.POST['txtsireccion']
    celular = request.POST['txtcelular']
    email = request.POST['email']
    
    empleados = Empleados.objects.get(Id_Empleado=Id_Empleado)
    empleados.nombre = nombre
    empleados.apellidos = apellidos
    empleados.sexo = sexo
    empleados.direccion = direccion
    empleados.celular = celular
    empleados.email = email
    empleados.save()
    return redirect('empleados')

def borrarEmpleados(request,Id_Empleado):
    empleados=Empleados.objects.get(Id_Empleado=Id_Empleado)
    empleados.delete()
    return redirect("empleados")