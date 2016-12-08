from django.contrib import admin
from writer.models import Section, Writer

class SectionAdmin(admin.ModelAdmin):
    search_fields = ['section', 'section_slug']
    list_display = ['section', 'section_slug', 'display_count']
    
class WriterAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'name_slug']
    #prepopulated_fields = {'name_slug': ('first_name', 'last_name')}
    fieldsets = (
        ('Section', {
            'fields': ('section',)
        }),
        ('Writer', {
            'fields': ('first_name', 'last_name', 'name_slug', 'title','photo', 'on_staff')
        }),
    )
    list_display = ['last_name', 'first_name', 'section', 'name_slug', 'title', 'on_staff']
    list_editable = ['on_staff']
    list_filter = ['on_staff', 'section']
    
#class SectionChoiceAdmin(admin.ModelAdmin):
#    search_fields = ['section',]
#    list_display = ['section', 'display_count']
    
admin.site.register(Section, SectionAdmin)
admin.site.register(Writer, WriterAdmin)
