import datetime

from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blogs.forms import ReviewForm, SignupForm, SigninForm
from blogs.models import Article, Category
from blogs.scrapper import scrap
from blogs.serializer import ArticleSerializer


def signin(req):
    if req.user.is_authenticated:
        messages.info(req, "User already logged in")
        return redirect("blogs:list")

    if req.method=="POST":
        form = SigninForm(req.POST)
        # username = req.POST["username"]
        # password = req.POST["password"]
        username = form["username"].value()
        password = form["password"].value()
        user = authenticate(req, username=username,  password=password)
        if user is not None:
            login(req, user)
            messages.success(req, "Successfully logged in")
            return redirect("blogs:list")
        else:
            messages.error(req, "Invalid Username or Password")
    else:
        form = SigninForm()
    return render(req, "blogs/signin.html", {"form":form})


def signout(req):
    logout(req)
    messages.info(req, "Logged out successfully")
    return redirect("blogs:signin")


def signup(req):
    if req.user.is_authenticated:
        messages.info(req, "User already logged in")
        return redirect("blogs:list")

    if req.method == "POST":
        form = SignupForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(req, "User created successfully")
            return redirect("blogs:signin")
        else:
            messages.info(req, "Invalid form")
    else:
        form = SignupForm()
    return render(req, "blogs/signup.html", {"form": form})


def blog_list(req):
    articles = Article.objects.filter(published=True)
    data = {"data":articles}
    return render(req, "blogs/index.html", data)


def blog_details(req, id):
    article = Article.objects.get(id=id)
    article.views += 1
    article.save()
    form = ReviewForm()
    return render(req, "blogs/detail.html", {"article":article, "form":form})

def blog_review(req, id):
    if req.method == "POST":
        if req.user.is_authenticated:
            form = ReviewForm(req.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.created = datetime.datetime.now()
                review.article = Article.objects.get(id=id)
                review.user = req.user
                review.save()
                messages.success(req, "Review saved successfully")
        else:
            messages.error(req, "Login required to post reviews")
            return redirect("blogs:signin")
    return redirect("blogs:detail", id)

def blog_new(req):
    data = scrap(req.GET.get("url"))
    if data:
        cat = Category.objects.get(pk=1)
        article = Article()
        article.author = "New Author"
        article.category = cat
        article.created = datetime.datetime.now()
        article.title = data["title"]
        article.description = data["description"]
        article.published = True
        article.save()
        messages.success(req, "Post saved")
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
