from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Empleados(models.Model):
    Id_Empleado =  models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    sexo =  models.CharField(max_length=10)
    direccion  = models.CharField(max_length=100)
    celular  = models.IntegerField()
    email  = models.EmailField(max_length=50)

    class Meta: 
        db_table =  "Empleados"
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def  __str__(self):
        return self.nombre + " - " + f"{self.celular}"