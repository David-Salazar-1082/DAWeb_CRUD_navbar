from django.urls import  path
from Sucursales_app import views

urlpatterns = [
    path('sucursales', views.inicio_vistaSucursales, name='sucursales'),
    path('registrarSucursales/', views.registrarSucursales, name='registrarSucursales'),
    path("seleccionarSucursales/<Id_Sucursal>",views.seleccionarSucursales,name="seleccionarSucursales"),
    path("editarSucursales/",views.editarSucursales,name="editarSucursales"),
    path("borrarSucursales/<Id_Sucursal>",views.borrarSucursales,name="borrarSucursales"),
] 