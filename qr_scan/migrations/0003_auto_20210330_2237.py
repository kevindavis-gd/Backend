# Generated by Django 3.1.6 on 2021-03-31 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_auto_20210330_2159'),
        ('qr_scan', '0002_auto_20210325_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='buildingID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='locations.building'),
        ),
    ]