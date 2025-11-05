from django.contrib import admin
from .models import Dimensiones
from .forms import FormDimensiones


@admin.register(Dimensiones)
class DimensionesAdmin(admin.ModelAdmin):
    form = FormDimensiones

    # ==========================
    # CONFIGURACIÓN VISUAL
    # ==========================
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_per_page = 10

    # ==========================
    # AGRUPACIÓN DE CAMPOS
    # ==========================
    fieldsets = (
        ("Información de la Dimensión", {
            "fields": ("nombre",)
        }),
    )

    # ==========================
    # CONSULTA OPTIMIZADA
    # ==========================
    def get_queryset(self, request):
        """Optimiza la carga de datos (por si luego hay relaciones)."""
        qs = super().get_queryset(request)
        return qs

    # ==========================
    # MENSAJES PERSONALIZADOS
    # ==========================
    def save_model(self, request, obj, form, change):
        """Mensaje al crear o actualizar una dimensión"""
        super().save_model(request, obj, form, change)
        if change:
            self.message_user(request, f"✅ Dimensión '{obj.nombre}' actualizada correctamente.")
        else:
            self.message_user(request, f"✅ Dimensión '{obj.nombre}' creada correctamente.")

    def delete_model(self, request, obj):
        """Mensaje al eliminar una dimensión"""
        super().delete_model(request, obj)
        self.message_user(request, f"🗑️ La dimensión '{obj.nombre}' fue eliminada correctamente.")
