from django.db import models


class Servicio(models.Model):
    """Servicio que ofrece el negocio (ejemplo; adáptalo a tu proyecto)."""
        
    titulo = models.CharField(max_length=100) # texto corto
    artista = models.CharField(max_length=100) # texto largo, opcional
    lanzamiento = models.DateField(null=False, blank=False) 

    class Meta:
        ordering = ["titulo"] # orden por defecto de las consultas
        verbose_name_plural = "servicios" # cómo se ve en el admin
    
    def __str__(self):
    #   Texto que Django muestra cuando imprime el objeto (admin, shell)
        return self.artista