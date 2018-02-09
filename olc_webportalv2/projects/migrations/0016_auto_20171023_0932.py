# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-23 13:32
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20171023_0857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genesipprresults',
            options={'verbose_name_plural': 'Genesippr Results'},
        ),
        migrations.AlterModelOptions(
            name='sendsketchresults',
            options={'verbose_name_plural': 'Sendsketch Results'},
        ),
        migrations.AlterField(
            model_name='project',
            name='requested_jobs',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('genesipprv2', 'GenesipprV2'), ('sendsketch', 'sendsketch')], max_length=22),
        ),
    ]
