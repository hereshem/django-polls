from django.urls import path

from blogs.views import blog_list, blog_details, blog_new, blog_api, blog_review

app_name = "blogs"


urlpatterns = [
    path('', blog_list, name="list"),
    path('<int:id>/', blog_details, name="detail"),
    path('<int:id>/review/', blog_review, name="review"),
    path('post/', blog_new, name="new"),
    path('api/', blog_api, name="new"),

]
