# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-13 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_blogpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='title',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='blogtitle',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]