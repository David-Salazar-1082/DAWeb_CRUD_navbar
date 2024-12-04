from django.urls import path
from Productos_app import views

urlpatterns = [
    path('productos', views.inicio_vistaProducto, name='productos'),
    path('registrarProducto/', views.registrarProducto, name='registrarProducto'),
    path("seleccionarProducto/<Id_Producto>",views.seleccionarProducto,name="seleccionarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto"),
    path("borrarProducto/<Id_Producto>" ,views.borrarProducto,name="borrarProducto")

]