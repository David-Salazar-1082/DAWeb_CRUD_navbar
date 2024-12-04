from django.db import models

# Create your models here.

class Venta(models.Model):
    Id_Venta = models.CharField(max_length=50,primary_key=True)
    total = models.FloatField()
    fecha = models.DateField()
    Id_Empleado = models.IntegerField()
    Id_Cliente = models.IntegerField()
    Id_Sucursal = models.IntegerField()
    Productos_Comprados = models.CharField(max_length=100)
    
    class Meta: 
        db_table =  "Ventas"
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
    
    def __str__(self):
        return self.Productos_Comprados