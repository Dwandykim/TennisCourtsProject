# Generated by Django 4.0.6 on 2022-07-29 22:29

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis_court_locations', '0003_remove_locations_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicCourts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('park_name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=300)),
                ('latitude', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('longitude', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('location_address', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=25)),
                ('fees', models.CharField(max_length=10)),
                ('lights', models.CharField(max_length=10)),
                ('indoor', models.CharField(max_length=10)),
                ('courts', models.CharField(max_length=10)),
            ],
        ),
    ]
