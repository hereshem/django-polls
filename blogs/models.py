from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
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
    # description = models.TextField()
    author = models.CharField(max_length=250)
    created = models.DateTimeField()
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    published = models.BooleanField()

    def __str__(self):
        return self.title


class Review(models.Model):
    rate = models.IntegerField(default=10, validators=[MaxValueValidator(10), MinValueValidator(1)])
    review = models.TextField(blank=True)
    created = models.DateTimeField()
    published = models.BooleanField(default=True)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.review
