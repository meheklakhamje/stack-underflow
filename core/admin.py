from django.contrib import admin

from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "votes", "views")
    search_fields = ("title", "body", "author__username")
    readonly_fields = ("votes", "views")