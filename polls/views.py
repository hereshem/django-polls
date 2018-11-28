from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Question

# Create your views here.

def hello_world(req):
    return HttpResponse("<h1>Hello World</h1>")


def question_list(req):
    questions = Question.objects.all()
    data = {"data": questions, "count":len(questions), "a":"apple"}
    return render(req, "polls/index.html", data)


def question_detail(req, id):
    return render(req, "polls/detail.html")


def question_vote(req, id):
    return render(req, "polls/vote.html")