#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views import generic
from story.models import Story
from writer.models import Section, Writer
import logging
logging.basicConfig(filename='/Users/smosqueda/django-playground/booger/projects/tbtdjangocms/writer/writer.log',level=logging.INFO)

class IndexView(generic.ListView):
    template_name = 'writer/index.html'
    context_object_name = 'latest_writer_list'    
    #story_list = get_list_or_404(Story.published_objects,section__section_slug=section.section_slug)
    #writer_list = dict{}
    one = None
    two = None
    three = None
    def get_queryset(self):
        section = get_object_or_404(Section, section_slug="news")
        writer_list = Writer.objects.filter(section__section_slug="news")[:3]
        one_story = None
        two_story = None
        three_story = None
        if writer_list:
            logging.error("HAVE A writer_list")
            #one = writer_list.get(name_slug='john-romano')
            #two = writer_list.get(name_slug='sue-carlton')
            #three = writer_list.get(name_slug='ernest-hooper')            
            one = writer_list[0]
            two = writer_list[1]
            three = writer_list[2]
            
            #logging.error("one's stuff %s %s %s" % (one.first_name, one.bio, one.section.section_slug))
            if one:
                one_story = Story.objects.filter(section=section).filter(writers__in=[one]).order_by("-publish_date").select_related()
                if one_story is not None:
                    r_story = one_story[0];
                    logging.error("story details: %s %s" % (r_story.headline, r_story.body_text))
                else:
                    logging.error("don't have one_story")
            if two:
                two_story = Story.objects.filter(section=section).filter(writers__in=[two]).order_by("-publish_date").select_related()
                if two_story is not None:
                    s_story = two_story[0];
                    logging.error("story details: %s %s" % (s_story.headline, s_story.body_text))
                else:
                    logging.error("don't have two_story")
            if three:
                three_story = Story.objects.filter(section=section).filter(writers__in=[three]).order_by("-publish_date").select_related()
                if three_story is not None:
                    e_story = three_story[0];
                    logging.error("story details: %s %s" % (e_story.headline, e_story.body_text))
                else:
                    logging.error("don't have three_story")            
            writer_list = dict(one_writer=one, one_story=r_story, two_writer=two, two_story=s_story, three_writer=three, three_story=e_story)
            return writer_list
        else:
            logging.error("no writer_list")
            return ""
    #return render_to_response('index.html',{'object': story, 'year': year, 'month': month, 'day': day, 'slug': slug, 'edition': ed, #'facebook_id' : settings.FACEBOOK_APP_ID })

    #stories = Story.published_objects.filter(section=section).order_by('-publish_date').select_related()[:5]

    #Originally this
    #def get_queryset(self):
     #   return Writer.objects.all()[:3]


'''
class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
'''
