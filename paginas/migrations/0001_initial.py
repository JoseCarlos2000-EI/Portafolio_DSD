# Generated by Django 3.1.7 on 2021-03-06 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=60)),
            ],
        ),
    ]
