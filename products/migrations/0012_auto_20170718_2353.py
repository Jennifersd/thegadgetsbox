# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-18 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20170718_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='oldprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
