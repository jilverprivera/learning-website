from django.contrib import admin

from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subcategory', 'uuid', 'price', 'compare_price', 'status',)
    list_display_links = ('title', 'uuid')
    list_filter = ('subcategory', )
    list_editable = ('price', )
    search_fields = ('uuid', 'title', 'description', )
    list_per_page = 25


admin.site.register(Course, CourseAdmin)
admin.site.register(Section)
admin.site.register(Comment)
admin.site.register(WhatLearnt)
admin.site.register(Requisite)
admin.site.register(Resource)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Rating)
# admin.site.register(CoursesLibrary)
# admin.site.register(PaidCoursesLibrary)


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title',)
    list_display_links = ('uuid', 'title', )
    list_filter = ('uuid', )
    search_fields = ('uuid', 'content', 'title')
    list_per_page = 25
admin.site.register(Episode, EpisodeAdmin)

# class SectorAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title',)
#     list_editable = ('title', )
#     list_per_page = 10
# admin.site.register(Sector, SectorAdmin)
