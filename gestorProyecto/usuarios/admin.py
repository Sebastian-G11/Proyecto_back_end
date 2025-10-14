from django.contrib import admin
from .models import Usuarios
from .forms import FormUsuario

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    form = FormUsuario  
    list_display = ('nombre', 'apellido', 'email', 'rol')
    list_filter = ('rol',)
    search_fields = ('nombre', 'apellido', 'email')
    ordering = ('nombre',)
    list_per_page = 10 

    fieldsets = (
        ("Información Personal", {
            "fields": ("nombre", "apellido", "email")
        }),
        ("Rol del Usuario", {
            "fields": ("rol",)
        }),
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            self.message_user(request, "✅ Usuario actualizado correctamente.")
        else:
            self.message_user(request, "✅ Usuario creado correctamente.")

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        self.message_user(request, f"🗑️ El usuario '{obj}' fue eliminado correctamente.")
