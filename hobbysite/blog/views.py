from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article
from .forms import ArticleForm, CommentForm
from user_management.models import Profile


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        queryset = super().get_queryset()

        user_articles = queryset.filter(author=self.request.user.profile)
        other_articles = queryset.exclude(author=self.request.user.profile)
        queryset = list(user_articles) + list(other_articles)

        return queryset

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('blog:article-detail', kwargs={ 'pk': self.object.pk })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        author_articles = Article.objects.filter(author=article.author).exclude(pk=article.pk)[:2]
        context['author_articles'] = author_articles
        context['form'] = self.form_class()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            form.instance.author = profile
            form.instance.article = self.get_object()
            form.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blog/article_create.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse_lazy('blog:article-detail', kwargs={ 'pk': self.object.pk })
    
    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'blog/article_update.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse_lazy('blog:article-detail', kwargs={ 'pk': self.object.pk })