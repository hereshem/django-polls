from django.shortcuts import render

# Create your views here.
from blogs.models import Article


def blog_list(req):
    articles = Article.objects.filter(published=True)
    data = {"data":articles}
    return render(req, "blogs/index.html", data)


def blog_details(req, id):
    article = Article.objects.get(id=id)
    return render(req, "blogs/detail.html", {"article":article})