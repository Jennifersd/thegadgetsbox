# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-13 17:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_shop'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shop',
        ),
    ]