# Generated by Django 3.1.1 on 2020-10-01 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InputOutput', '0002_auto_20201001_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docmas',
            name='docId',
        ),
    ]