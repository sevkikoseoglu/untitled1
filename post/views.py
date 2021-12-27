from django.shortcuts import render
from django.views.generic import ListView
from post.models import Article


class ArticleList(ListView):
    queryset = Article.objects.order_by('-created_date')
    template_name = 'post_list.html'
