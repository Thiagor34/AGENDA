# Generated by Django 4.2 on 2023-05-11 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_contatos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatos',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='contatos',
            name='telefone',
            field=models.CharField(max_length=14),
        ),
    ]
