
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubActividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad', models.CharField(choices=[('Actividad1', 'Actividad 1'), ('Actividad2', 'Actividad 2')], max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('grado_aprobacion', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
