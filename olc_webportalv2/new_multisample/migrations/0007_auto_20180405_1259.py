# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-05 12:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_multisample', '0006_amrresult_species'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmulti',
            name='gdcs_file',
        ),
        migrations.RemoveField(
            model_name='projectmulti',
            name='genesippr_file',
        ),
        migrations.RemoveField(
            model_name='projectmulti',
            name='results_created',
        ),
        migrations.RemoveField(
            model_name='projectmulti',
            name='serosippr_file',
        ),
        migrations.RemoveField(
            model_name='projectmulti',
            name='sixteens_file',
        ),
    ]
