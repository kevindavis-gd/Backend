# Generated by Django 3.1.6 on 2021-04-01 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_scan', '0008_auto_20210330_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='scanDate',
            field=models.CharField(max_length=100),
        ),
    ]
