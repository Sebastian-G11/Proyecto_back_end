from django.db import migrations

def poblar_usuarios(apps, schema_editor):
    Usuarios = apps.get_model('usuarios', 'Usuarios')
    Roles = apps.get_model('usuarios', 'Roles')
    
    # Obtener los roles
    rol_admin = Roles.objects.get(rol_id=1) 
    rol_usuario = Roles.objects.get(rol_id=2) 
    
    # Crear usuarios iniciales
    usuarios_iniciales = [
        {
            'nombre': 'Admin',
            'apellido': 'Sistema',
            'email': 'admin@sistema.com',
            'password': 'admin123',  
            'rol': rol_admin
        },
        {
            'nombre': 'Usuario',
            'apellido': 'Demo',
            'email': 'usuario@sistema.com',
            'password': 'user123', 
            'rol': rol_usuario
        },
    ]
    
    for user_data in usuarios_iniciales:
        Usuarios.objects.get_or_create(
            email=user_data['email'],
            defaults=user_data
        )

def eliminar_usuarios(apps, schema_editor):
    Usuarios = apps.get_model('usuarios', 'Usuarios')
    Usuarios.objects.filter(
        email__in=['admin@sistema.com', 'usuario@sistema.com']
    ).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_usuarios_password'), 
    ]

    operations = [
        migrations.RunPython(poblar_usuarios, eliminar_usuarios),
    ]