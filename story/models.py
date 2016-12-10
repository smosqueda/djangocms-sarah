from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from django.db.models import Q
from writer.models import Section, Writer

class PublishedObjectsManager(models.Manager):
    def get_queryset(self):
        rightnow = datetime.datetime.now()
        if settings.CMS:
            return super().get_queryset().filter(Q(is_live=True) | Q(preview=True))
        else:
            return super().get_queryset().filter(is_live=True).exclude(publish_date__gt=rightnow)
        
class Story(models.Model):
    section = models.ManyToManyField(Section, related_name="section_set", help_text="More than one section allowed")
    headline = models.CharField(max_length=100)
    headline_slug = models.SlugField(unique=True,help_text="Don't change this unless you know what you're doing.")
    twitter_headline = models.CharField(max_length=100)
    fb_headline = models.CharField(max_length=100)
    body_text = HTMLField()
    preview = models.BooleanField()    
    writers = models.ManyToManyField(Writer, related_name="writer_set", help_text="More than one writer allowed")
    other_writers = models.CharField(max_length=200)
    is_live = models.BooleanField()
    photo = models.ImageField(blank=True)
    objects = models.Manager()
    publish_date = models.DateTimeField(help_text="This is the publication date of your item.")
    class Meta:
        ordering = ['-publish_date']
        verbose_name_plural = "Stories"
    @property
    def unified_date(self):
        return self.publish_date
    def get_canonical_url(self):
        #return "http://www.politifact.com/%s/statements/%s%s/%s/" % (self.edition.edition_slug, self.ruling_date.strftime('%Y/%b/%d/').lower(), self.speaker.name_slug, self.ruling_headline_slug)
        return "/%s/%s/%s/" % (self.section.section_slug, self.headline_slug, self._id)
    story_url = property(get_canonical_url)
    def __str__(self):
        return "%s" % (self.headline)
    
