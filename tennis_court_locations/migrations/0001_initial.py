# Generated by Django 4.0.6 on 2022-07-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('park_name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=25)),
                ('fees', models.CharField(max_length=10)),
                ('lights', models.CharField(max_length=10)),
                ('indoor', models.CharField(max_length=10)),
                ('courts', models.CharField(max_length=10)),
            ],
        ),
    ]
