# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-20 06:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'video分类信息', 'verbose_name_plural': 'video分类信息'},
        ),
        migrations.AlterField(
            model_name='videos',
            name='kind',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.Category', verbose_name='video分类'),
        ),
    ]
