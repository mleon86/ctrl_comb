from django.db import models

class Mark(models.Model):
    descript = models.CharField(
        max_length=50,
        unique=True)
    
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
    
    def __str__(self):
        return f"{self.descript}"
    

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
        verbose_name_plural = "Modelos"
        db_table_comment = "Modelos de Vehículos"
