# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 21:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chirps', '0003_auto_20170402_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='chirp',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
