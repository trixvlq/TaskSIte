# Generated by Django 4.2.4 on 2023-08-15 17:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Task.status'),
        ),
    ]
