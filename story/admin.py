from django.contrib import admin
from story.models import Story
from writer.models import Section, Writer

class StoryAdmin(admin.ModelAdmin):
    search_fields = ['headline', 'headline_slug']
    list_display = ['headline', 'headline_slug', 'preview', 'is_live',]
    #prepopulated_fields = {'headline_slug': ('headline'),}
    fieldsets = (
        ('Sections', {
            'fields': ('section',)
        }),
        ('Story', {
            'fields': ('headline', 'headline_slug', 'photo', 'body_text','preview', 'other_writers','is_live','publish_date',)
        }),
        ('Authors', {
            'fields': ('writers',)
        }),
    )
    list_editable = ['is_live']
    list_filter = ['is_live', 'section']
    
admin.site.register(Story, StoryAdmin)
