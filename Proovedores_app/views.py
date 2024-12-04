from django.shortcuts import render,redirect
from .models import Proovedor

# Create your views here.

def inicio_vistaProovedor(request):
    losproovedores=Proovedor.objects.all()
    return render(request, 'gestionarProovedores.html', {'proovedor': losproovedores})


def registrarProovedor(request):
    Id_Proovedor = request.POST['txtid']
    nombre = request.POST['txtnombre']
    tipo_producto = request.POST['txttipoproducto']
    ubicacion = request.POST['txtubicacion']
    cant_producto = request.POST['txtcant_producto']
    horarios = request.POST['txthorarios']
    telefono = request.POST['txttelefono']

    registrarProovedor =Proovedor.objects.create(Id_Proovedor=Id_Proovedor, nombre=nombre, tipo_producto=tipo_producto, 
                                            ubicacion=ubicacion, cant_producto=cant_producto, horarios=horarios, telefono=telefono)
    return redirect('proovedores')
    
def seleccionarProovedor(request,Id_Proovedor):
    proovedor=Proovedor.objects.get(Id_Proovedor=Id_Proovedor)
    return render(request,"editarProovedores.html",{"misproovedores":proovedor})

def editarProovedor(request):
    Id_Proovedor = request.POST['txtid']
    nombre = request.POST['txtnombre']
    tipo_producto = request.POST['txttipoproducto']
    ubicacion = request.POST['txtubicacion']
    cant_producto = request.POST['txtcant_producto']
    horarios = request.POST['txthorarios']
    telefono = request.POST['txttelefono']
    
    proovedor=Proovedor.objects.get(Id_Proovedor=Id_Proovedor)
    proovedor.Id_Proovedor=Id_Proovedor
    proovedor.nombre = nombre
    proovedor.tipo_producto = tipo_producto
    proovedor.ubicacion = ubicacion
    proovedor.cant_producto = cant_producto
    proovedor.horarios = horarios
    proovedor.telefono = telefono
    proovedor.save()
    return redirect('proovedores')

def borrarProovedor(request,Id_Proovedor):
    proovedor=Proovedor.objects.get(Id_Proovedor=Id_Proovedor)
    proovedor.delete()
    return redirect('proovedores')
