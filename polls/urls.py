from django.urls import path

from polls.views import hello_world, question_list, question_detail, question_vote

urlpatterns = [
    path('', question_list),
    path('<int:id>/', question_detail),
    path('<int:id>/vote/', question_vote),
]
