# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-18 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20170718_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='oldprice',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
