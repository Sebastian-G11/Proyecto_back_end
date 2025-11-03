from django.db import migrations

def poblar_estados(apps, schema_editor):
    Estados = apps.get_model('acciones', 'Estados')
    estados_iniciales = [
        {'estado_id': 1, 'nombre': 'Pendiente'},
        {'estado_id': 2, 'nombre': 'En Progreso'},
        {'estado_id': 3, 'nombre': 'Completado'},
        {'estado_id': 4, 'nombre': 'Cancelado'},
    ]
    for estado_data in estados_iniciales:
        Estados.objects.get_or_create(
            estado_id=estado_data['estado_id'],
            defaults={'nombre': estado_data['nombre']}
        )

def eliminar_estados(apps, schema_editor):
    Estados = apps.get_model('acciones', 'Estados')
    Estados.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('acciones', '0008_accion_estado'),
    ]

    operations = [
        migrations.RunPython(poblar_estados, eliminar_estados),
    ]