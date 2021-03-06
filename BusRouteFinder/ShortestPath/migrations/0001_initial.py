# Generated by Django 3.2.4 on 2021-07-17 04:20

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('buses', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='ShortestPath.station')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='ShortestPath.station')),
            ],
        ),
    ]
