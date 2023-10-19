from django.db import models

class Mark(models.Model):
    descript = models.CharField(
        max_length=50,
        unique=True)
    def __str___(self):
        return self.descript
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
    
class Modelo(models.Model):
    descript = models.CharField(
        max_length=50,
        db_comment = "Descripcion del Modelo de Vehículo"  
    )
    mark = models.ForeignKey(Mark,
                                   on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.mark} - {self.descript}"
    
    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos de Vehiculos"
