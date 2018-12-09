from django.contrib import admin

# Register your models here.
from blogs.models import Article, Category, Review


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "category", "views", "published"]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Review)