# Generated by Django 3.1.6 on 2021-03-31 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_auto_20210330_2159'),
        ('qr_scan', '0005_auto_20210330_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkin',
            name='buildingID',
        ),
        migrations.AddField(
            model_name='checkin',
            name='room',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='locations.room'),
        ),
    ]
