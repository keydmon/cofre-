from django.db import models
class Tarea(models.Model):
    tarea=models.CharField(max_length=100)
    def  __str__(self):
        return self.tarea 

# la funcion __str__ sirve para mostrar 
# de esta forma las tablas se gestionan por python directamente y no se deben crear en msql
# la clase es la tabla la que es Tarea el otro tarea vendria a ser un atributo
# Create your models here.
