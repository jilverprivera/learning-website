from django.contrib import admin

from .models import Course, CoursesLibrary, PaidCoursesLibrary


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subcategory', 'price', 'discount_price', 'discount_time', 'status',)
    list_display_links = ('title',)
    list_filter = ('title', 'price')
    list_editable = ('price', 'discount_price', 'discount_time', 'status')
    search_fields = ('uuid', 'title', 'description', )
    list_per_page = 25


admin.site.register(Course, CourseAdmin)
admin.site.register(CoursesLibrary)
admin.site.register(PaidCoursesLibrary)
