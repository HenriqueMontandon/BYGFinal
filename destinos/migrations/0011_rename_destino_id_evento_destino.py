# Generated by Django 4.2.7 on 2023-11-28 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinos', '0010_alter_destino_empresaid_delete_empresa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='destino_id',
            new_name='destino',
        ),
    ]