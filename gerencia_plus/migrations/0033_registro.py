# Generated by Django 4.1.7 on 2023-08-22 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia_plus', '0032_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
            ],
        ),
    ]
