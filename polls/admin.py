from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["title", "created"]
    list_filter = ["title", "created"]
    search_fields = ["title"]
    fields = ["title", "created"]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


# admin.site.register(Choice)
