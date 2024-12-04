# Generated by Django 5.1 on 2024-12-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('Id_Venta', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('total', models.FloatField()),
                ('fecha', models.DateField()),
                ('Id_Empleado', models.IntegerField()),
                ('Id_Cliente', models.IntegerField()),
                ('Id_Sucursal', models.IntegerField()),
                ('Productos_Comprados', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'db_table': 'Ventas',
            },
        ),
    ]
