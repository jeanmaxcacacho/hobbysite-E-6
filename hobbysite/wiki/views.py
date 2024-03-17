from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article, ArticleCategory

class ArticleList(ListView):
    model = Article
    template_name = 'articlesList.html' 
    context_object_name = 'articles' 
    
class ArticleDetail(DetailView):
    model = Article
    template_name = 'articleDetails.html'
    context_object_name = 'article'

