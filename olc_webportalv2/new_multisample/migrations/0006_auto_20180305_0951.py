# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-05 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_multisample', '0005_auto_20180305_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='new_multisample.ProjectMulti'),
        ),
    ]
