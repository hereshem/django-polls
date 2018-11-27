from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice

    pass

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["created", "id", "title"]
    list_filter = ["title", "created"]
    search_fields = ["title"]
    fields = ["created", "title"]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


# admin.site.register(Choice)