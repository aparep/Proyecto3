from django.db import models

class Tarea(models.Model):
    descripcion = models.CharField(max_length=100)
    duracionseg = models.IntegerField()

    def __str__(self) -> str:
        return self.descripcion

class Responsable(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre

class Local(models.Model):
    establecimiento = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.establecimiento
