from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from django.db.models import Q
from story.models import Story

class PublishedObjectsManager(models.Manager):
    def get_queryset(self):
        rightnow = datetime.datetime.now()
        if settings.CMS:
            return super().get_queryset().filter(Q(is_live=True) | Q(preview=True))
        else:
            return super().get_queryset().filter(is_live=True).exclude(publish_date__gt=rightnow)

class Carousel(models.Model):
    name = models.CharField(max_length=100, help_text='A friendly name for your setup')
    storyOne = models.ForeignKey(Story, related_name="storyone_set", help_text='Second Slide will come from this story')
    captionOne = models.CharField(max_length=100, help_text='For headline override')
    storyTwo = models.ForeignKey(Story, related_name="storytwo_set", help_text='Third Slide will come from this story')
    captionTwo = models.CharField(max_length=100, help_text='For headline override')
    storyThree = models.ForeignKey(Story, related_name="storythree_set", help_text='First Slide will come from this story')
    captionThree = models.CharField(max_length=100, help_text='For headline override')
    storyFour = models.ForeignKey(Story, null=True, blank=True, related_name="storyfour_set", help_text='(Optional) - Fourth Slide will come from this story')
    captionFour = models.CharField(max_length=100, null=True, blank=True, help_text='For headline override')
    publish_date = models.DateTimeField(help_text="This is the publication date of your Carousel.")
    is_live = models.BooleanField()
    preview = models.BooleanField()
    published_objects = models.Manager() #PublishedObjectsManager()
    css = HTMLField(null=True, blank=True, help_text='If left blank, it will be provided for you.')
    js = HTMLField(null=True, blank=True, help_text='If left blank, it will be provided for you.')    
    class Meta:
        ordering = ['-publish_date']
        verbose_name_plural = "Carousels"
    @property
    def unified_date(self):
        return self.publish_date    
    def __str__(self):
        return "%s" % (self.name)

