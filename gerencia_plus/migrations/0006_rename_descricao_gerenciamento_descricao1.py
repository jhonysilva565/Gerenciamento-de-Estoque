# Generated by Django 4.1.7 on 2023-06-02 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia_plus', '0005_rename_nome_gerenciamento_nome_produto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gerenciamento',
            old_name='descricao',
            new_name='descricao1',
        ),
    ]