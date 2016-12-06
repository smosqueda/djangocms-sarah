# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='bio',
            field=djangocms_text_ckeditor.fields.HTMLField(),
        ),
    ]
