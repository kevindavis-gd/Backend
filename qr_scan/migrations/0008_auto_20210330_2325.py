# Generated by Django 3.1.6 on 2021-03-31 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_scan', '0007_auto_20210330_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='checkInTime',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='checkOutTime',
            field=models.CharField(max_length=100),
        ),
    ]