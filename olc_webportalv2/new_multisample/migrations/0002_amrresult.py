# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-22 17:26
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_multisample', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AMRResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results_dict', django.contrib.postgres.fields.hstore.HStoreField()),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amr_results', to='new_multisample.Sample')),
            ],
            options={
                'verbose_name_plural': 'AMR Results',
            },
        ),
    ]
