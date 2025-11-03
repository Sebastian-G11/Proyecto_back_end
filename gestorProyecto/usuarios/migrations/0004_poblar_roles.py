from django.db import migrations

def poblar_roles(apps, schema_editor):
    Roles = apps.get_model('usuarios', 'Roles')
    roles_iniciales = [
        {'rol_id': 1, 'nombre': 'Administrador'},
        {'rol_id': 2, 'nombre': 'Usuario'},
    ]
    for rol_data in roles_iniciales:
        Roles.objects.get_or_create(
            rol_id=rol_data['rol_id'],
            defaults={'nombre': rol_data['nombre']}
        )

def eliminar_roles(apps, schema_editor):
    Roles = apps.get_model('usuarios', 'Roles')
    Roles.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuarios_rol'),  # Reemplaza con tu migración anterior
    ]

    operations = [
        migrations.RunPython(poblar_roles, eliminar_roles),
    ]