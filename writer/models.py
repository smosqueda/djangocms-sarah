from django.db import models
#from ckeditor.fields import RichTextField as HTMLField
from djangocms_text_ckeditor.fields import HTMLField

class Section(models.Model):
    section = models.CharField(max_length=50)
    section_slug = models.SlugField(unique=True)
    display_count = models.IntegerField(default=3,help_text="This only effects the Writerbox plugin display.")
    
    def __str__(self):
        return self.section


class Writer(models.Model):
    section = models.ForeignKey(Section)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    name_slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    email_address = models.EmailField()
    bio = HTMLField()
    photo = models.ImageField(blank=True) #, upload_to='times/writers/')
    on_staff = models.BooleanField(default=True)
    class Meta:
        ordering = ['last_name']
    def get_absolute_url(self):
        return "/%s/writer/%s/" % (self.section.section_slug, self.name_slug)
    def __str__(self):
        return "%s %s, %s" % (self.first_name, self.last_name, self.title)
    
'''class SectionChoice(models.Model):
    section = models.ForeignKey(Section)
    display_count = models.IntegerField(default=3)
    
    def __str__(self):
        return "%s %s" % (self.section.section, self.display_count)
'''