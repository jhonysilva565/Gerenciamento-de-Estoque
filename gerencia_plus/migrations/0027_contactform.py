# Generated by Django 4.1.7 on 2023-06-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia_plus', '0026_rename_mensagem_contato_message_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]