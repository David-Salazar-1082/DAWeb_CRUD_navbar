from django.db import models

# Create your models here.

class Clientes(models.Model):
    Id_Cliente = models.IntegerField(primary_key=True)
    nombre  = models.CharField(max_length=50)
    apellidos  = models.CharField(max_length=50)
    edad   = models.IntegerField()
    sexo  = models.CharField(max_length=10)
    dni   = models.CharField(max_length=15)
    fecha_nacimiento   = models.DateField()

    class Meta: 
        db_table =  "Clientes"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def    __str__(self):
        return self.nombre + " " + self.apellidos