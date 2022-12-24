# Generated by Django 4.0.1 on 2022-12-24 03:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('data', models.DateField(blank=True, default=datetime.datetime(2022, 12, 24, 0, 33, 24, 242740))),
                ('status', models.BooleanField(default=False)),
                ('descricao', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
