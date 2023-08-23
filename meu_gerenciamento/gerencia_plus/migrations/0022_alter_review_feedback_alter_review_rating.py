# Generated by Django 4.1.7 on 2023-06-25 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia_plus', '0021_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='feedback',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('5', 'Excelente'), ('4', 'Muito Bom'), ('3', 'Bom'), ('2', 'Regular'), ('1', 'Ruim')], max_length=10),
        ),
    ]
