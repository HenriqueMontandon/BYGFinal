# Generated by Django 4.2.7 on 2023-11-30 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinos', '0011_rename_destino_id_evento_destino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_fim',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_inicio',
            field=models.DateField(),
        ),
    ]