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

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('blog:article-detail', kwargs={ 'pk': self.object.pk })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = self.form_class(article=self.object)
        return context
    
    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        form.instance.article = self.object
        return super().form_valid(form)

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