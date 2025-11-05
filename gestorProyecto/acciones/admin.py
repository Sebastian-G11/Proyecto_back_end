from django.contrib import admin
from .models import Accion, VerificacionAccion
from .forms import AccionForm, VerificacionForm


class VerificacionAccionInline(admin.TabularInline):
    model = VerificacionAccion
    form = VerificacionForm
    extra = 1
    min_num = 0
    verbose_name = "Medio de Verificación"
    verbose_name_plural = "Medios de Verificación"


@admin.register(Accion)
class AccionAdmin(admin.ModelAdmin):
    form = AccionForm
    inlines = [VerificacionAccionInline]

    # Columnas visibles en el listado
    list_display = (
        'nombre',
        'dimension_nombre',
        'responsable_nombre',
        'presupuesto_anual',
        'presupuesto_reajustado',
        'estado_nombre',
        'fecha_creacion',
        'fecha_modificacion',
    )

    list_filter = ('dimension', 'estado', 'responsable')
    search_fields = ('nombre', 'descripcion', 'responsable__nombre', 'dimension__nombre')
    ordering = ('-fecha_creacion',)
    list_per_page = 10

    def get_fieldsets(self, request, obj=None): 
        if obj:
            return (
                ("Información General", {
                    "fields": ("nombre", "descripcion", "dimension", "estado")
                }),
                ("Responsable", {
                    "fields": ("responsable",)
                }),
                ("Presupuestos", {
                    "fields": ("presupuesto_anual", "presupuesto_reajustado")
                }),
            )
        else:
            return (
                ("Información General", {
                    "fields": ("nombre", "descripcion", "dimension", "estado")
                }),
                ("Responsable", {
                    "fields": ("responsable",)
                }),
                ("Presupuestos", {
                    "fields": ("presupuesto_anual",)
                }),  
            )

    
    # ==========================
    # 🔹 OPTIMIZACIÓN DE CONSULTAS
    # ==========================
    def get_queryset(self, request):
        """Optimiza con select_related para evitar consultas repetidas."""
        qs = super().get_queryset(request)
        return qs.select_related('dimension', 'estado', 'responsable')

    # ==========================
    # 🔹 CAMPOS PERSONALIZADOS
    # ==========================
    def dimension_nombre(self, obj):
        return obj.dimension.nombre if obj.dimension else "-"
    dimension_nombre.short_description = "Dimensión"

    def responsable_nombre(self, obj):
        return obj.responsable.nombre if obj.responsable else "-"
    responsable_nombre.short_description = "Responsable"

    def estado_nombre(self, obj):
        return obj.estado.nombre if obj.estado else "-"
    estado_nombre.short_description = "Estado"

    # ==========================
    # 🔹 MENSAJES PERSONALIZADOS
    # ==========================
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            self.message_user(request, f"✅ Acción '{obj.nombre}' actualizada correctamente.")
        else:
            self.message_user(request, f"✅ Acción '{obj.nombre}' creada correctamente.")

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        self.message_user(request, f"🗑️ La acción '{obj.nombre}' fue eliminada correctamente.")


@admin.register(VerificacionAccion)
class VerificacionAccionAdmin(admin.ModelAdmin):
    form = VerificacionForm

    list_display = ('nombre', 'accion_nombre', 'url')
    list_filter = ('accion',)
    search_fields = ('nombre', 'accion__nombre')
    ordering = ('nombre',)
    list_per_page = 10

    fieldsets = (
        ("Detalles del Medio de Verificación", {
            "fields": ("accion", "nombre", "url")
        }),
    )

    # Mostrar nombre legible de la acción
    def accion_nombre(self, obj):
        return obj.accion.nombre if obj.accion else "-"
    accion_nombre.short_description = "Acción"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            self.message_user(request, f"✅ Medio de verificación '{obj.nombre}' actualizado correctamente.")
        else:
            self.message_user(request, f"✅ Medio de verificación '{obj.nombre}' creado correctamente.")

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        self.message_user(request, f"🗑️ El medio de verificación '{obj.nombre}' fue eliminado correctamente.")
