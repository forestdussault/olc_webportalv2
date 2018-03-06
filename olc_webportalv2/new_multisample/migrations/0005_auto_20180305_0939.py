# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-05 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_multisample', '0004_auto_20180302_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='description',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='sample',
            name='file_R1',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sample',
            name='file_R2',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
