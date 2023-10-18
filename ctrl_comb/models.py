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
    
