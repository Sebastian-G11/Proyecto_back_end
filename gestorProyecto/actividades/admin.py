from django.contrib import admin
from .models import Actividad
from .forms import ActividadForm


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    form = ActividadForm

    list_display = (
        'nombre',
        'accion_nombre',
        'responsable_nombre',
        'estado_nombre',
        'fecha_creacion',
        'fecha_actualizacion',
    )

    list_filter = ('estado', 'responsable', 'fecha_creacion')
    search_fields = ('nombre', 'responsable__nombre', 'accion_id__nombre')
    ordering = ('-fecha_creacion',)
    list_per_page = 10

    fieldsets = (
        ("Información General", {
            "fields": ("nombre", "accion_id", "estado")
        }),
        ("Responsable", {
            "fields": ("responsable",)
        }),
    
    )


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('estado', 'accion_id', 'responsable')

    def accion_nombre(self, obj):
        return obj.accion_id.nombre if obj.accion_id else "-"
    accion_nombre.short_description = "Acción"

    def responsable_nombre(self, obj):
        return obj.responsable.nombre if obj.responsable else "-"
    responsable_nombre.short_description = "Responsable"

    def estado_nombre(self, obj):
        return obj.estado.nombre if obj.estado else "-"
    estado_nombre.short_description = "Estado"


    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            self.message_user(request, f"✅ Actividad '{obj.nombre}' actualizada correctamente.")
        else:
            self.message_user(request, f"✅ Actividad '{obj.nombre}' creada correctamente.")

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        self.message_user(request, f"🗑️ La actividad '{obj.nombre}' fue eliminada correctamente.")
