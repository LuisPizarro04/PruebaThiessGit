from django.contrib import admin
from .models import Hojas_mantencione, Asistencia_Mantenimiento


# Register your models here.

class Hojas_mantencioneInline(admin.TabularInline):
    model = Hojas_mantencione
    extra = 1


class Hojas_mantencioneAdmin(admin.ModelAdmin):
    list_display = ('id', 'folio_mantencion', 'numero_equipo', 'horas_intervencion', 'descripcion_trabajo', 'ot',
                    'horometro',)
    search_fields = ('folio_mantencion', 'numero_equipo',)


class Asistencia_MantenimientoAdmin(admin.ModelAdmin):
    inlines = [Hojas_mantencioneInline]
    list_display = ('folio_h_m', 'nombre_trabajador', 'dia_turno', 'fecha_mantencion', 'rut_trabajador', 'turno',
                    'hora_entrada', 'hora_salida',)
    search_fields = ('folio_h_m', 'nombre_trabajador', 'fecha_mantencion', 'rut_trabajador', 'turno',)
    filter_horizontal = ('equipo',)


admin.site.register(Asistencia_Mantenimiento,Asistencia_MantenimientoAdmin)
admin.site.register(Hojas_mantencione, Hojas_mantencioneAdmin)
