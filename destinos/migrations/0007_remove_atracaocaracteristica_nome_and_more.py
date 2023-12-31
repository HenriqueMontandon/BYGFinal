# Generated by Django 4.2.5 on 2023-11-28 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinos', '0006_atracaocaracteristica_atracao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atracaocaracteristica',
            name='nome',
        ),
        migrations.AddField(
            model_name='atracaocaracteristica',
            name='atracao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='destinos.destino'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='atracaocaracteristica',
            name='caracteristica_tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='destinos.preferenciatipo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='atracaocaracteristica',
            name='nota',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Atracao',
        ),
    ]
