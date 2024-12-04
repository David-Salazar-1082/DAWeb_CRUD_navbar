from django.db import models

# Create your models here.

class Proovedor(models.Model):
    Id_Proovedor = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    cant_producto = models.IntegerField()
    horarios = models.TimeField()
    telefono = models.IntegerField()
    
    class Meta: 
        db_table =  "Proovedores"
        verbose_name = "Proovedor"
        verbose_name_plural = "Proovedores"
    
    def __str__(self):
        return self.nombre
