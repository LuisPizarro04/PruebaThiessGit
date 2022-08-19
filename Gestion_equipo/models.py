from django.db import models


# Create your models here.

class Equipo(models.Model):
    num_equipo = models.CharField(max_length=20, primary_key=True)
    nombre_quipo = models.CharField(max_length=100, blank=False, null=False)
    tipo_equipo = models.CharField(max_length=100, blank=True, null=False)
    modelo_equipo = models.CharField(max_length=100, blank=False, null=False)
    marca_equipo = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.num_equipo
