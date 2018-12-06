
from rest_framework import serializers

from blogs.models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "published"]


class ArticleSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    created = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S")

    class Meta:
        model = Article
        fields = ["title", "description", "views", "published", "category", "created"]