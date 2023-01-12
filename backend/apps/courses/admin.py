from django.contrib import admin

from .models import *
# from .models.


# admin.site.register(Pricing)
# admin.site.register(Subscription)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subcategory', 'uuid', 'price', 'discount_price', 'status',)
    list_display_links = ('title', 'uuid')
    list_filter = ('title', 'price')
    list_editable = ('price', 'discount_price')
    search_fields = ('uuid', 'title', 'description', )
    list_per_page = 25


admin.site.register(Course, CourseAdmin)
# admin.site.register(Section)
# # admin.site.register(Comment)
# admin.site.register(WhatLearnt)
# # admin.site.register(Requisite)
# admin.site.register(Resource)
# admin.site.register(Question)
# admin.site.register(Answer)
# admin.site.register(Vote)
# admin.site.register(CoursesLibrary)
# admin.site.register(PaidCoursesLibrary)


# class LessonAdmin(admin.ModelAdmin):
#     list_display = ('uuid', 'title',)
#     list_display_links = ('uuid', 'title', )
#     list_filter = ('uuid', )
#     search_fields = ('uuid', 'content', 'title')
#     list_per_page = 25


# admin.site.register(Lesson, LessonAdmin)
