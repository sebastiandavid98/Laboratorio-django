from django.db import models

class Asistencia(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    presente = models.BooleanField()

    def __str__(self):
        return self.nombre