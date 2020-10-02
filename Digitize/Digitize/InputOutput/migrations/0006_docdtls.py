# Generated by Django 3.1.1 on 2020-10-01 14:25

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('InputOutput', '0005_auto_20201001_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='docDtls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docId', models.CharField(max_length=500)),
                ('buyer', models.CharField(max_length=100)),
                ('billTo', jsonfield.fields.JSONField()),
                ('optional', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'DocDtls',
            },
        ),
    ]