# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-08 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0006_project_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.TextField(),
        ),
    ]
