from django.db import models
from cms.models import CMSPlugin
from writer.models import Section, Writer
from story.models import Story


class SectionPluginModel(CMSPlugin):
    section = models.ForeignKey(Section)

    def __unicode__(self):
        return self.section
    
class WriterPluginModel(CMSPlugin):
    writer = models.ForeignKey(Writer)

    def __unicode__(self):
        return self.writer
    
class StoryPluginModel(CMSPlugin):
    story = models.ForeignKey(Story)

    def __unicode__(self):
        return self.story
