# Generated by Django 3.1.2 on 2020-11-16 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20201116_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vehicleAvatar',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
