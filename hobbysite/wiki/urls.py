from django.urls import path
from . import views

urlpatterns = [
    
    path('articles', views.ArticleList.as_view(), name='article_list'),
    path('article/<int:pk>', views.ArticleDetail.as_view(), name='article_detail'),
    
]