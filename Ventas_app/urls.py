from django.urls import path
from Ventas_app import views

urlpatterns = [
    path('ventas', views.inicio_vistaVenta, name='ventas'),
    path('registrarVenta/', views.registrarVenta, name='registrarVenta'),
    path("seleccionarVenta/<Id_Venta>",views.seleccionarVenta,name="seleccionarVenta"),
    path("editarVenta/",views.editarVenta,name="editarVenta"),
    path("borrarVenta/<Id_Venta>" ,views.borrarVenta,name="borrarVenta")

]
