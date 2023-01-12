from django.contrib import admin

from .models import Section


class SectionAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'section_number')
    list_display_links = ('uuid', 'title', )
    list_filter = ('uuid',)
    list_editable = ('section_number',)
    search_fields = ('uuid', 'title', 'section_number',)
    list_per_page = 25


admin.site.register(Section, SectionAdmin)
