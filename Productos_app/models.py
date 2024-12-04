from django.db import models

# Create your models here.

class Producto(models.Model):
    Id_Producto = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    proovedor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    
    class Meta: 
        db_table =  "Productos"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
    def __str__(self):
        return self.nombre