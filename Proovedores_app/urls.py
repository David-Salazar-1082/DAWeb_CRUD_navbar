from django.urls import path
from Proovedores_app import views

urlpatterns = [
    path('proovedores', views.inicio_vistaProovedor, name='proovedores'),
    path('registrarProovedor/', views.registrarProovedor, name='registrarProovedor'),
    path("seleccionarProovedor/<Id_Proovedor>",views.seleccionarProovedor,name="seleccionarProovedor"),
    path("editarProovedor/",views.editarProovedor,name="editarProovedor"),
    path("borrarProovedor/<Id_Proovedor>" ,views.borrarProovedor,name="borrarProovedor")

]