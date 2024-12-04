from django.urls import  path
from Clientes_app import views

urlpatterns = [
    path('clientes', views.inicio_vistaClientes, name='clientes'),
    path('registrarClientes/', views.registrarClientes, name='registrarClientes'),
    path("seleccionarClientes/<Id_Cliente>",views.seleccionarClientes,name="seleccionarClientes"),
    path("editarClientes/",views.editarClientes,name="editarClientes"),
    path("borrarClientes/<Id_Cliente>",views.borrarClientes,name="borrarClientes"),
] 