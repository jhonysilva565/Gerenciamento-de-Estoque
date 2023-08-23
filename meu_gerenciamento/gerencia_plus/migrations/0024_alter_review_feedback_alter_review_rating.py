# Generated by Django 4.1.7 on 2023-06-25 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia_plus', '0023_delete_avaliar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='feedback',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('Excelente', 'Excelente'), ('Bom', 'Bom'), ('Regular', 'Regular'), ('Ruim', 'Ruim')], max_length=10),
        ),
    ]
