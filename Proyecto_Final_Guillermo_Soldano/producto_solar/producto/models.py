from django.db import models

class Categorias(models.Model):
    categorias = models.CharField(max_length = 100, null=False, blank =False)
    


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categorias, on_delete = models.SET_NULL, null = True, blank = True)
    #imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre
