from django.contrib import admin

from .models import Course, CoursesLibrary, PaidCoursesLibrary


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subcategory', 'uuid',
                    'price', 'discount_price', 'status',)
    list_display_links = ('title', 'uuid')
    list_filter = ('title', 'price')
    list_editable = ('price', 'discount_price')
    search_fields = ('uuid', 'title', 'description', )
    list_per_page = 25


admin.site.register(Course, CourseAdmin)
admin.site.register(CoursesLibrary)
admin.site.register(PaidCoursesLibrary)
