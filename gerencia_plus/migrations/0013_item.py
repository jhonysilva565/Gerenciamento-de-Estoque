# Generated by Django 4.1.7 on 2023-06-10 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia_plus', '0012_delete_produtoexcluido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('descricao', models.TextField()),
                ('peso', models.FloatField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fornecedor', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('data_entrada', models.DateField()),
            ],
        ),
    ]
