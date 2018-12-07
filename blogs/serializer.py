
from rest_framework import serializers

from blogs.models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "published"]


class ArticleSerializer(serializers.ModelSerializer):

    # category = serializers.StringRelatedField()
    # category = CategorySerializer(read_only=True)
    # created = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S")
    short_description = serializers.SerializerMethodField()
    # description = serializers.SerializerMethodField()

    def get_short_description(self, model):
        return model.description[:20]

    def get_description(self,ob):
        return ob.description[:10]

    class Meta:
        model = Article
        fields = ["id", "title", "description", "views", "published", "category", "created", "short_description"]

    def create(self, validated_data):
        print(self.data)
        print(validated_data)
        cat = Category.objects.get(title=self.data["category"])
        art = Article.objects.create(**validated_data)
        if cat != None:
            art.category = cat
        art.save()
        return art