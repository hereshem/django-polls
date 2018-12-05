from django.urls import path

from blogs.views import blog_list, blog_details

app_name = "blogs"

urlpatterns = [
    path('', blog_list, name="list"),
    path('<int:id>/', blog_details, name="detail"),
]
