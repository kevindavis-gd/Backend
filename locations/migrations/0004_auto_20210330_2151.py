# Generated by Django 3.1.6 on 2021-03-31 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20210330_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='buildingCapacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='building',
            name='numberOfRooms',
            field=models.IntegerField(),
        ),
    ]
