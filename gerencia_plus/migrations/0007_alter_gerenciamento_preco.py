# Generated by Django 4.1.7 on 2023-06-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia_plus', '0006_rename_descricao_gerenciamento_descricao1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gerenciamento',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
