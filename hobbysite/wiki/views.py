from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article, ArticleCategory

class ArticleList(ListView):
    model = Article
    template_name = 'wiki/article_list.html'
    
class ArticleDetail(DetailView):
    model = Article
    template_name = 'wiki/article_detail.html'

