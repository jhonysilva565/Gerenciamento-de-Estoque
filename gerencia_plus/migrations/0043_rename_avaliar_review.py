# Generated by Django 4.2.5 on 2023-10-08 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia_plus', '0042_rename_review_avaliar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Avaliar',
            new_name='Review',
        ),
    ]