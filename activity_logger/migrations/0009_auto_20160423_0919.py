# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('activity_logger', '0008_auto_20160423_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='path',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activity_logger.Path', verbose_name='Path'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='deprecated_path',
            field=models.CharField(max_length=256, null=True, verbose_name='Path'),
        ),
    ]