from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Article, ArticleCategory, Comment
from django.db.models import Exists, OuterRef



class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'wiki/articlesList.html' 
    context_object_name = 'articles' 

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.annotate(
                has_comments=Exists(
                    Comment.objects.filter(article_id=OuterRef('pk'), author=self.request.user)
                )
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = ArticleCategory.objects.all()
        context['categories'] = categories
        return context



class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki/articleDetails.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        category = article.category
        other_articles = Article.objects.filter(category=category).exclude(id=article.id)[:2]
        context['other_articles'] = other_articles

        return context



class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'wiki/articleCreate.html'
    fields = ['title', 'category', 'entry', 'header_image']
    success_url = reverse_lazy('article_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticleCategory.objects.all()  # Add this line to pass categories to the template
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'wiki/articleUpdate.html'
    fields = ['title', 'category', 'entry', 'header_image']
    success_url = reverse_lazy('article_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['category'].queryset = ArticleCategory.objects.all()
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = self.request.user
        return initial

    def form_valid(self, form):
        return super().form_valid(form)
