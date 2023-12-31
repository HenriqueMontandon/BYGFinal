# Generated by Django 4.2.7 on 2023-11-27 01:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('destinos', '0002_preferenciatipo_preferencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='CNPJ',
            new_name='cnpj',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='nomeFantasia',
            new_name='endereco',
        ),
        migrations.RenameField(
            model_name='list',
            old_name='Nome',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='destino',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='list',
            name='atracoes',
        ),
        migrations.AddField(
            model_name='destino',
            name='coordenadas',
            field=models.CharField(default='(-23.4339, -45.0833)', max_length=100),
        ),
        migrations.AddField(
            model_name='destino',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destino',
            name='empresaid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='destinos.empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destino',
            name='preco',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='criacao_data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='delecao_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='email_contato',
            field=models.EmailField(default='aloaloalo', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='nome_fantasia',
            field=models.CharField(default='ubatuba', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='razao_social',
            field=models.CharField(default='ola user', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='telefone',
            field=models.CharField(default=124455512, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list',
            name='comentario',
            field=models.CharField(default='aaaaaaaaaaaa eu to maluco', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list',
            name='data_alteracao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='list',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list',
            name='descricao',
            field=models.CharField(default='bacana', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list',
            name='duracao',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list',
            name='nota',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destino',
            name='destino_url',
            field=models.URLField(default='eu nao sei'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_delecao', models.DateTimeField(null=True)),
                ('comentario', models.CharField(max_length=500, null=True)),
                ('nota', models.FloatField(null=True)),
                ('destino_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos.destino')),
                ('roteiro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos.list')),
            ],
        ),
        migrations.AlterField(
            model_name='destino',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos.categoria'),
        ),
    ]
