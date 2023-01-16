from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'lesson', 'accepted_answer', 'date_created')
    list_display_links = ('title',)
    list_filter = ('title', 'lesson', 'user')
    search_fields = ('title', 'lesson', )
    list_per_page = 25

admin.site.register(Question, QuestionAdmin)
