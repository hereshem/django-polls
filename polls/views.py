from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from polls.models import Question

# Create your views here.

def hello_world(req):
    return HttpResponse("<h1>Hello World</h1> <br> Click <a href='/polls'>here</a> to continue")


def question_list(req):
    page = int(req.GET.get("page", "1"))
    start = (page-1)*20
    end = page*20-1
    questions = Question.objects.all().order_by("title")[start:end]
    data = {"data": questions, "count":len(questions), "a":"apple"}
    return render(req, "polls/index.html", data)


def question_detail(req, id):
    question = Question.objects.get(pk=id)
    data = {"question": question}
    return render(req, "polls/detail.html", data)


def question_vote(req, id):
    question = get_object_or_404(Question, pk=id)
    try:
        choice_id = req.POST["choice"]
        choice = question.choice_set.get(pk=choice_id)
        choice.votes += 1
        choice.save()
    except:
        pass
    return redirect("/polls/%d/" % (id))

    # return redirect("/polls/" + str(id) + "/")
    # return redirect("/polls/{}/".format(id))
    # return render(req, "polls/vote.html")