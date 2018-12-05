from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Article(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.CharField(max_length=250)
    created = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    published = models.BooleanField()

    def __str__(self):
        return self.title