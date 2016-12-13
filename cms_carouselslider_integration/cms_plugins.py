from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from carousel.models import Carousel
from cms_carouselslider_integration.models import CarouselSliderPluginModel
from django.shortcuts import get_object_or_404 #, get_list_or_404, render
from django.utils.translation import ugettext as _


class CarouselSliderPluginPublisher(CMSPluginBase):
    model = CarouselSliderPluginModel  # model where plugin data are saved
    module = _("CarouselSlider")
    name = _("CarouselSlider Plugin")  # name of the plugin in the interface
    render_template = "cms_carouselslider_integration/carouselslider_plugin.html"

    def render(self, context, instance, placeholder):
        #section = get_object_or_404(Section, section_slug=section_param)
        carousel_name = instance
        carousel = get_object_or_404(Carousel, name=carousel_name)
        context.update({'carousel': carousel})
        return context

plugin_pool.register_plugin(CarouselSliderPluginPublisher)  # register the plugin
