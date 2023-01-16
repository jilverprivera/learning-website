from django.contrib import admin

from .models import Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'message', 'accepted')
    list_display_links = ('user', )
    list_editable = ('accepted',)
    search_fields = ('uuid', 'user', 'description', )
    list_per_page = 25


admin.site.register(Answer, AnswerAdmin)
