# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'A friendly name for your setup', max_length=100)),
                ('captionOne', models.CharField(help_text=b'For headline override', max_length=100)),
                ('captionTwo', models.CharField(help_text=b'For headline override', max_length=100)),
                ('captionThree', models.CharField(help_text=b'For headline override', max_length=100)),
                ('captionFour', models.CharField(help_text=b'For headline override', max_length=100, null=True, blank=True)),
                ('publish_date', models.DateTimeField(help_text=b'This is the publication date of your Carousel.')),
                ('is_live', models.BooleanField()),
                ('preview', models.BooleanField()),
                ('css', djangocms_text_ckeditor.fields.HTMLField(help_text=b'If left blank, it will be provided for you.', null=True, blank=True)),
                ('js', djangocms_text_ckeditor.fields.HTMLField(help_text=b'If left blank, it will be provided for you.', null=True, blank=True)),
                ('storyFour', models.ForeignKey(related_name='storyfour_set', blank=True, to='story.Story', help_text=b'(Optional) - Fourth Slide will come from this story', null=True)),
                ('storyOne', models.ForeignKey(related_name='storyone_set', to='story.Story', help_text=b'Second Slide will come from this story')),
                ('storyThree', models.ForeignKey(related_name='storythree_set', to='story.Story', help_text=b'First Slide will come from this story')),
                ('storyTwo', models.ForeignKey(related_name='storytwo_set', to='story.Story', help_text=b'Third Slide will come from this story')),
            ],
            options={
                'ordering': ['-publish_date'],
                'verbose_name_plural': 'Carousels',
            },
        ),
    ]
