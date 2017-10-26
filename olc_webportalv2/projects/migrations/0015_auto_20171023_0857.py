# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-23 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20171020_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendsketchresults',
            name='ani',
            field=models.CharField(default='N/A', max_length=256),
        ),
        migrations.AddField(
            model_name='sendsketchresults',
            name='complt',
            field=models.CharField(default='N/A', max_length=256),
        ),
        migrations.AddField(
            model_name='sendsketchresults',
            name='contam',
            field=models.CharField(default='N/A', max_length=256),
        ),
        migrations.AddField(
            model_name='sendsketchresults',
            name='gseqs',
            field=models.CharField(default='N/A', max_length=256),
        ),
        migrations.AddField(
            model_name='sendsketchresults',
            name='gsize',
            field=models.CharField(default='N/A', max_length=256),
        ),
        migrations.AddField(
            model_name='sendsketchresults',
            name='kid',
            field=models.CharField(default='N/A', max_length=256),
        ),
        migrations.AddField(
            model_name='sendsketchresults',
            name='matches',
            field=models.CharField(default='N/A', max_length=256),
        ),
        migrations.AddField(
            model_name='sendsketchresults',
            name='nohit',
            field=models.CharField(default='N/A', max_length=256),
        ),
        migrations.AddField(
            model_name='sendsketchresults',
            name='taxid',
            field=models.CharField(default='N/A', max_length=256),
        ),
        migrations.AddField(
            model_name='sendsketchresults',
            name='taxname',
            field=models.CharField(default='N/A', max_length=256),
        ),
        migrations.AddField(
            model_name='sendsketchresults',
            name='unique',
            field=models.CharField(default='N/A', max_length=256),
        ),
        migrations.AddField(
            model_name='sendsketchresults',
            name='wkid',
            field=models.CharField(default='N/A', max_length=256),
        ),
    ]
