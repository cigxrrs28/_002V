# Generated by Django 3.1 on 2021-06-21 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='tipo_consulta',
            field=models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'sugerencias'], [3, 'felicitaciones']]),
        ),
    ]
