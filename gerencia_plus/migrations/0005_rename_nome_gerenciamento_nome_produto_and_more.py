# Generated by Django 4.1.7 on 2023-06-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia_plus', '0004_gerenciamento_delete_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gerenciamento',
            old_name='nome',
            new_name='nome_produto',
        ),
        migrations.AlterField(
            model_name='gerenciamento',
            name='quantidade',
            field=models.IntegerField(),
        ),
    ]
