from django.db import models


class Producto(models.Model):
        codigo = models.IntegerField(unique=True)  # Asegúrate de que sea único
        cantidad = models.IntegerField()
        descripcion = models.TextField()
        categoria = models.CharField(max_length=100)
        precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
        costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
        
        def __str__(self):
            return self.descripcion


# Create your models here.
