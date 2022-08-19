from django.db import models


# Create your models here.

class Supervisore(models.Model):
    rut_supervisor = models.CharField(max_length=10, primary_key=True)
    nombres_supervisor = models.CharField(max_length=100, blank=False, null=False)
    apellidos_supervisor = models.CharField(max_length=100, blank=False, null=False)
    fecha_nac_supervisor = models.DateField(blank=False, null=False)
    telefono_supervisor = models.IntegerField(blank=False, null=False)
    email_supervisor = models.EmailField(blank=False, null=False)
