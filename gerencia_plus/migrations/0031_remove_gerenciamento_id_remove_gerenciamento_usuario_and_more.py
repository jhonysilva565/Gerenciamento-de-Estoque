# Generated by Django 4.1.7 on 2023-07-31 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia_plus', '0030_remove_gerenciamento_id_usuario_gerenciamento_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gerenciamento',
            name='id',
        ),
        migrations.RemoveField(
            model_name='gerenciamento',
            name='usuario',
        ),
        migrations.AddField(
            model_name='gerenciamento',
            name='id_usuario',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]