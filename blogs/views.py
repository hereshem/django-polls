import datetime

from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import blogs
from blogs.forms import ReviewForm
from blogs.models import Article, Category
from blogs.scrapper import scrap
from blogs.serializer import ArticleSerializer


def blog_list(req):
    articles = Article.objects.filter(published=True)
    data = {"data":articles}
    return render(req, "blogs/index.html", data)


def blog_details(req, id):
    article = Article.objects.get(id=id)
    form = ReviewForm()
    return render(req, "blogs/detail.html", {"article":article, "form":form})

def blog_review(req, id):
    if req.method == "POST":
        form = ReviewForm(req.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.created = datetime.datetime.now()
            review.article = Article.objects.get(id=id)
            review.user = req.user
            review.save()
    return redirect("blogs:detail", id)

def blog_new(req):
    data = scrap(req.GET.get("url"))
    if data:
        cat = Category.objects.get(pk=1)
        article = Article()
        article.author = "hello"
        article.category = cat
        article.created = datetime.datetime.now()
        article.title = data["title"]
        article.description = data["description"]
        article.published = True
        article.save()
    return redirect("blogs:list")

@api_view(['GET', 'POST'])
def blog_api(req):
    if req.method == "GET":
        articles = Article.objects.filter(published=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif req.method == "POST":
        serializer = ArticleSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)