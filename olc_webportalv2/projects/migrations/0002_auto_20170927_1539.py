# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-27 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import olc_webportalv2.projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='file_R1',
            field=models.FileField(blank=True, upload_to=olc_webportalv2.projects.models.make_path),
        ),
        migrations.AlterField(
            model_name='project',
            name='file_R2',
            field=models.FileField(blank=True, upload_to=olc_webportalv2.projects.models.make_path),
        ),
    ]