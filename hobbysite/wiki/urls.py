from django.urls import path
from . import views

app_name = "wiki"

urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/add/', views.ArticleCreateView.as_view(), name='article_add'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:article_id>/comment/add/', views.CommentCreateView.as_view(), name='comment_create'),
]
