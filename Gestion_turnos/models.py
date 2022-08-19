from django.db import models

# Create your models here.

class Turno(models.Model):
    id_turno = models.AutoField(primary_key=True)
    nombre_turno = models.CharField(max_length=100, blank=False, null=False)