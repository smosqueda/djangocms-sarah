# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section', models.CharField(max_length=50)),
                ('section_slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('name_slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=254)),
                ('bio', ckeditor.fields.RichTextField()),
                ('photo', models.ImageField(upload_to=b'', blank=True)),
                ('on_staff', models.BooleanField(default=True)),
                ('section', models.ForeignKey(to='writer.Section')),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
    ]
