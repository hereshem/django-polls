from django.urls import path

from polls.views import hello_world, question_list, question_detail, question_vote

app_name = "polls"

urlpatterns = [
    path('', question_list, name="list"),
    path('<int:id>/', question_detail, name="detail"),
    path('<int:id>/vote/', question_vote, name="vote"),
]
