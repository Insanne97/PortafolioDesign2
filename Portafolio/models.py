from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='Portafolio/imagen/')
    enlace = models.URLField(blank=True)
    
    def __str__(self) -> str:
        nombreProyecto = 'Titulo: ' + self.titulo
        return nombreProyecto
