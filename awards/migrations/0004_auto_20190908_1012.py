# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-08 10:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_auto_20190906_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='post',
            new_name='description',
        ),
    ]
