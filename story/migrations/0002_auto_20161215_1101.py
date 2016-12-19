# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='author',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='story',
            name='byline',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='story',
            name='metatags',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='story',
            name='sectionPath',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='story',
            name='sourceid',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
