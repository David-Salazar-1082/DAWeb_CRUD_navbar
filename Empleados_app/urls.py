from django.urls import  path
from Empleados_app import views

urlpatterns = [
    path('empleados', views.inicio_vistaEmpleados, name='empleados'),
    path('registrarEmpleados/', views.registrarEmpleados, name='registrarEmpleados'),
    path("seleccionarEmpleados/<Id_Empleado>",views.seleccionarEmpleados,name="seleccionarEmpleados"),
    path("editarEmpleados/",views.editarEmpleados,name="editarEmpleados"),
    path("borrarEmpleados/<Id_Empleado>",views.borrarEmpleados,name="borrarEmpleados"),
] 