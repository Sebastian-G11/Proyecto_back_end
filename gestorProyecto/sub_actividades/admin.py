from django.contrib import admin
from .models import SubActividad
from .forms import SubActividadForm


@admin.register(SubActividad)
class SubActividadAdmin(admin.ModelAdmin):
    form = SubActividadForm  

    # ==========================
    # CONFIGURACIÓN VISUAL
    # ==========================
    list_display = ('nombre', 'grado_aprobacion', 'fecha_creacion')
    list_filter = ('actividad',)
    search_fields = ('nombre', 'actividad__nombre')  # ✅ relación corregida
    ordering = ('nombre',)
    list_per_page = 10 

    fieldsets = (
        ("Información de Subactividad", {
            "fields": ("nombre", "actividad", "grado_aprobacion")
        }),
    )

    # ==========================
    # MENSAJES PERSONALIZADOS
    # ==========================
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            self.message_user(request, f"✅ Subactividad '{obj.nombre}' actualizada correctamente.")
        else:
            self.message_user(request, f"✅ Subactividad '{obj.nombre}' creada correctamente.")

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        self.message_user(request, f"🗑️ La subactividad '{obj.nombre}' fue eliminada correctamente.")
