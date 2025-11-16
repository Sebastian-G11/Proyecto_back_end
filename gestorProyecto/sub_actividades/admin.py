from django.contrib import admin
from .models import SubActividad
from .forms import SubActividadForm


@admin.register(SubActividad)
class SubActividadAdmin(admin.ModelAdmin):
    form = SubActividadForm  


    list_display = ('nombre','actividad', 'grado_aprobacion', 'fecha_creacion','fecha_actualizacion')
    list_filter = ('actividad',)
    search_fields = ('nombre', 'actividad__nombre')
    ordering = ('nombre',)
    list_per_page = 10 

    def get_fieldsets(self, request, obj=None):
        """
        Si se está creando → incluye 'actividad'.
        Si se está editando → no lo muestra.
        """
        if obj: 
            return (
                ("Información de Subactividad", {
                    "fields": ("nombre", "grado_aprobacion")
                }),
            )
        else: 
            return (
                ("Información de Subactividad", {
                    "fields": ("actividad", "nombre", "grado_aprobacion")
                }),
            )



    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            self.message_user(request, f"✅ Subactividad '{obj.nombre}' actualizada correctamente.")
        else:
            self.message_user(request, f"✅ Subactividad '{obj.nombre}' creada correctamente.")

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        self.message_user(request, f"🗑️ La subactividad '{obj.nombre}' fue eliminada correctamente.")
