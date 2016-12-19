# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='display_count',
            field=models.IntegerField(default=3, help_text=b'This only effects the Writerbox plugin display.'),
        ),
    ]
