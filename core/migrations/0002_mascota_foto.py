# Generated by Django 3.2.3 on 2021-06-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(null=True, upload_to='mascotas'),
        ),
    ]
