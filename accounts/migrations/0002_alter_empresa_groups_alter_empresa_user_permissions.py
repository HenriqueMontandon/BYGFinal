# Generated by Django 4.2.7 on 2023-11-27 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='groups',
            field=models.ManyToManyField(related_name='empresa_groups', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='user_permissions',
            field=models.ManyToManyField(related_name='empresa_user_permissions', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
