# Generated by Django 4.2.6 on 2023-11-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinos', '0004_alter_list_duracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='comentario',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='nota',
            field=models.IntegerField(null=True),
        ),
    ]
