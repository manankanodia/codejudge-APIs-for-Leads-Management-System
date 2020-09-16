# Generated by Django 2.1 on 2020-09-16 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('mobile', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('location_type', models.CharField(blank=True, max_length=100)),
                ('location_string', models.CharField(blank=True, max_length=200)),
                ('status', models.CharField(default='Created', max_length=50)),
                ('communication', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
