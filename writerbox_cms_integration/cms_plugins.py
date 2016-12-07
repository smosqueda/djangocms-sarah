from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from polls_cms_integration.models import WriterboxPluginModel
from django.utils.translation import ugettext as _


class WriterboxPluginPublisher(CMSPluginBase):
    writer_model = WriterPluginModel  # model where plugin data are saved
    story_model = StoryPluginModel  # model where plugin data are saved
    section_model = SectionPluginModel  # model where plugin data are saved
    module = _("Writerbox")
    name = _("Writerbox Plugin")  # name of the plugin in the interface
    render_template = "writerbox_cms_integration/writerbox_plugin.html"

    def render(self, context, instance, placeholder):
        #context.update({'instance': instance})
        #return context

plugin_pool.register_plugin(WriterboxPluginPublisher)  # register the plugin
