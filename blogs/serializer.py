
from rest_framework import serializers

from blogs.models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "published"]


class ArticleSerializer(serializers.ModelSerializer):

    # Uncomment if category string is required
    # category = serializers.StringRelatedField()

    # Uncomment if Category object is required
    # category = CategorySerializer(read_only=True)

    # Uncomment if dateformat required
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")


    # short_description = serializers.SerializerMethodField()
    # def get_short_description(self, model):
    #     return model.description[:20]

    class Meta:
        model = Article
        fields = ["id", "title", "description", "views", "published", "category", "created"]

    def create(self, validated_data):
        print(self.data)
        print(validated_data)
        cat = Category.objects.get(id=self.data["category"])
        art = Article.objects.create(**validated_data)
        if cat != None:
            art.category = cat
        art.save()
        return art
