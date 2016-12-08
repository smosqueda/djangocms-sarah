# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=100)),
                ('headline_slug', models.SlugField(help_text=b"Don't change this unless you know what you're doing.", unique=True)),
                ('twitter_headline', models.CharField(max_length=100)),
                ('fb_headline', models.CharField(max_length=100)),
                ('body_text', djangocms_text_ckeditor.fields.HTMLField()),
                ('preview', models.BooleanField()),
                ('other_writers', models.CharField(max_length=200)),
                ('is_live', models.BooleanField()),
                ('photo', models.ImageField(upload_to=b'', blank=True)),
                ('publish_date', models.DateTimeField(help_text=b'This is the publication date of your item.')),
                ('section', models.ManyToManyField(help_text=b'More than one section allowed', related_name='section_set', to='writer.Section')),
                ('writers', models.ManyToManyField(help_text=b'More than one writer allowed', related_name='writer_set', to='writer.Writer')),
            ],
            options={
                'ordering': ['-publish_date'],
                'verbose_name_plural': 'Stories',
            },
        ),
    ]
