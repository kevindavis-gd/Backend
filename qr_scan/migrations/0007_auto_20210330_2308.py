# Generated by Django 3.1.6 on 2021-03-31 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_scan', '0006_auto_20210330_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkin',
            old_name='scanTime',
            new_name='checkInTime',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='checkIn',
        ),
        migrations.AddField(
            model_name='checkin',
            name='checkOutTime',
            field=models.TimeField(auto_now=True),
        ),
    ]
