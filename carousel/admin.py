from django.contrib import admin
from carousel.models import Carousel

class CarouselAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'captionOne', 'captionTwo', 'captionThree','captionFour','is_live','preview']
    fieldsets = (
        ('Carousel', {
            'fields': ('name','storyOne','captionOne','storyTwo','captionTwo','storyThree','captionThree','storyFour','captionFour','is_live','preview','publish_date')
        }),
        ('CSS', {
            'fields':
            ('css',)
        }),
        ('JS', {
            'fields':
            ('js',)
        }),
    )
    list_editable = ['is_live']
    list_filter = ['is_live', 'name']
    
admin.site.register(Carousel, CarouselAdmin)
