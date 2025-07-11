from django.contrib import admin

from .models import Choice, Question



admin.site.site_header = "Polls Admin"
admin.site.site_title = "Polls Admin Portal"
admin.site.index_title = "Bienvenue sur l'administration Polls"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
admin.site.register(Question, QuestionAdmin)

