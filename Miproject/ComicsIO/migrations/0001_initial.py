# Generated by Django 5.0.2 on 2024-03-10 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
                ('FechaDePublicacion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='el_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=100)),
                ('Texto', models.TextField()),
                ('fechaCreacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='OpinionDelComic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDelcomic', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('La_opinion', models.TextField(max_length=250)),
            ],
        ),
    ]
