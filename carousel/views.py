#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views import generic
from carousel.models import Carousel

import logging
#logging.basicConfig(filename='/Users/smosqueda/django-playground/booger/projects/tbtdjangocms/carousel/carousel.log',level=logging.INFO)

logging.basicConfig(filename='carousel.log',level=logging.INFO)

class IndexView(generic.ListView):
    template_name = 'carousel/index.html'
    context_object_name = 'carousel' 
    carousel = None
    logging.error("----------------------")
    logging.error("----------------------")
    def get_queryset(self):
        carousel_list = get_list_or_404(Carousel.published_objects)
        if carousel_list is not None:
            logging.error("------FOUND Carousel-----------")
            carousel = carousel_list[0]
        else:
            logging.error("------NO Carousel-----------")
        return carousel
