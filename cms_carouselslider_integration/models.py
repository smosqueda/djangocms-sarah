from django.db import models
from cms.models import CMSPlugin
from carousel.models import Carousel

class CarouselSliderPluginModel(CMSPlugin):
    carousel = models.ForeignKey(Carousel)

    def __unicode__(self):
        return self.carousel.name