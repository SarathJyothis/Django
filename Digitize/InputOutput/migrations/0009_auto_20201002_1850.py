# Generated by Django 3.1.1 on 2020-10-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InputOutput', '0008_auto_20201002_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docdtls',
            name='id',
        ),
        migrations.RemoveField(
            model_name='docmas',
            name='id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='userId',
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default='', max_length=500, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='docdtls',
            name='docId',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='docmas',
            name='docId',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
    ]
