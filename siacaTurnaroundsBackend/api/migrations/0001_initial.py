# Generated by Django 4.2.1 on 2023-06-01 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maquinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('combustible', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('imagen', models.CharField(max_length=50)),
            ],
        ),
    ]
