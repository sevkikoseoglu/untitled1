from django.urls import path
from post.views import ArticleList
urlpatterns = [
    path('', ArticleList.as_view()),
]