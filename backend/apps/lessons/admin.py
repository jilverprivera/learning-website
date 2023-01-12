from django.contrib import admin

from .models import Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'lesson_number')
    list_display_links = ('uuid', 'title', )
    list_filter = ('uuid',)
    list_editable = ('lesson_number',)
    search_fields = ('uuid', 'title', 'lesson_number',)
    list_per_page = 25


admin.site.register(Lesson, LessonAdmin)
