from django.contrib import admin
from .models import SolicitudMaterial
from .form import FormSolicitudMaterial


@admin.register(SolicitudMaterial)
class SolicitudMaterialAdmin(admin.ModelAdmin):
    form = FormSolicitudMaterial

    # ==========================
    # CONFIGURACIÓN VISUAL
    # ==========================
    list_display = (
        'actividad_id',
        'materiales_solicitados',
        'numero_orden',
        'valor_esperado',
        'valor_final',
        'codigo_factura',
        'fecha_creacion',
    )
    list_filter = ('actividad_id', 'fecha_creacion')
    search_fields = ('materiales_solicitados', 'numero_orden', 'codigo_factura')
    ordering = ('-fecha_creacion',)
    list_per_page = 10

    # ==========================
    # FIELDSETS DINÁMICOS
    # ==========================
    def get_fieldsets(self, request, obj=None):
        """
        Si se está creando → muestra 'valor_esperado' editable.
        Si se está editando → muestra 'valor_final' editable y 'valor_esperado' solo lectura.
        """
        if obj:  # Editando
            return (
                ("Información de la Solicitud", {
                    "fields": (
                        "actividad_id",
                        "materiales_solicitados",
                        "numero_orden",
                        "codigo_factura",
                    )
                }),
                ("Valores", {
                    "fields": ("valor_esperado", "valor_final")
                }),
            )
        else:  # Creando nuevo
            return (
                ("Información de la Solicitud", {
                    "fields": (
                        "actividad_id",
                        "materiales_solicitados",
                        "numero_orden",
                        "codigo_factura",
                    )
                }),
                ("Valores", {
                    "fields": ("valor_esperado",)
                }),
            )

    # ==========================
    # CAMPOS SOLO LECTURA
    # ==========================
    def get_readonly_fields(self, request, obj=None):
        """
        Durante la edición, 'valor_esperado' no se puede modificar.
        """
        if obj:
            return ('valor_esperado', 'fecha_creacion')
        return ('fecha_creacion',)

    # ==========================
    # MENSAJES PERSONALIZADOS
    # ==========================
    def save_model(self, request, obj, form, change):
        """Mensaje al crear o actualizar"""
        super().save_model(request, obj, form, change)
        if change:
            self.message_user(request, f"✅ La solicitud '{obj.numero_orden}' fue actualizada correctamente.")
        else:
            self.message_user(request, f"✅ La solicitud '{obj.numero_orden}' fue creada correctamente.")

    def delete_model(self, request, obj):
        """Mensaje al eliminar"""
        super().delete_model(request, obj)
        self.message_user(request, f"🗑️ La solicitud '{obj.numero_orden}' fue eliminada correctamente.")
