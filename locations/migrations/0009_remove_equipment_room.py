# Generated by Django 3.1.6 on 2021-04-12 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0008_auto_20210412_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='room',
        ),
    ]
