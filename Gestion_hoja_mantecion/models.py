from django.db import models
from Gestion_equipo.models import Equipo


# Create your models here.

class Asistencia_Mantenimiento(models.Model):
    folio_h_m = models.AutoField(primary_key=True)
    nombre_trabajador = models.CharField(max_length=200, blank=False, null=False)
    dia_turno = models.CharField(max_length=10, blank=False, null=False)
    fecha_mantencion = models.DateField(blank=False, null=False)
    rut_trabajador = models.CharField(max_length=10, blank=False, null=False)
    turno = models.CharField(max_length=10, blank=False, null=False)
    hora_entrada = models.TimeField(blank=False, null=False)
    hora_salida = models.TimeField(blank=False, null=False)
    equipo = models.ManyToManyField(Equipo, through='Hojas_mantencione', blank=False)

    """    class Meta:
            verbose_name = "Hoja de asistenacia diaria de mantención"
            verbose_name_plural = "Hojas de asistenacia diaria de mantención"
            ordering = ['folio_h_m']"""

    def __str__(self):
        return str(self.folio_h_m)


class Hojas_mantencione(models.Model):
    id = models.AutoField(primary_key=True)
    folio_mantencion = models.ForeignKey(Asistencia_Mantenimiento, on_delete=models.CASCADE, blank=False, null=False)
    numero_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, blank=False, null=False)
    horas_intervencion = models.IntegerField(blank=False, null=False)
    descripcion_trabajo = models.TextField(max_length=300, blank=False, null=False)
    ot = models.CharField(max_length=20, blank=False, null=False)
    horometro = models.IntegerField(blank=False, null=False)
