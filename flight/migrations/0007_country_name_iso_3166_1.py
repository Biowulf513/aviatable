# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0006_auto_20170823_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='name_ISO_3166_1',
            field=models.CharField(default=1, editable=False, max_length=3),
            preserve_default=False,
        ),
    ]
