# Generated by Django 3.2.7 on 2021-09-25 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_tipocliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='documento',
            field=models.CharField(choices=[('D', 'DPI'), ('C', 'CEDULA')], default='C', max_length=20),
        ),
    ]
