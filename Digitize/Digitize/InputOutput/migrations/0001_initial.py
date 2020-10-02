# Generated by Django 3.1.1 on 2020-10-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='digitizeDtls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=500)),
                ('docId', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'DigitizeDTLS',
            },
        ),
        migrations.CreateModel(
            name='docMas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docId', models.CharField(max_length=500)),
                ('origFileName', models.CharField(max_length=500)),
                ('filePath', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'DocMAS',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=500)),
                ('pwd', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]