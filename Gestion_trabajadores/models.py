from django.db import models

# Create your models here.


class Trabajadore(models.Model):
    rut_trabajador = models.CharField(max_length=10, primary_key=True)
    nombres_trabajador = models.CharField(max_length=100, blank=False, null=False)
    apellidos_trabajador = models.CharField(max_length=100, blank=False, null=False)
    fecha_nac_trabajador = models.DateField(blank=False, null=False)
    telefono_trabajador = models.IntegerField(blank=False, null=False)
    email_trabajador = models.EmailField(blank=False, null=False)