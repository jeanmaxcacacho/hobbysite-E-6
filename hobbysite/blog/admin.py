from django.contrib import admin
from .models import Article, ArticleCategory

class ArticleInline(admin.TabularInline):
    model = Article

class ArticleCategoryAdmin(admin.ModelAdmin):
    inlines = [ArticleInline,]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)

# Register your models here.