from django.db import models
'''
app_name: wiki
URLs: 
    List View: /wiki/articles
    Detail View: /wiki/article/1
Models:
> ArticleCategory
    > Name - max length is 255 characters ★
    > Description - text field ★
    Categories should be sorted by name in ascending order [?]
> Article
    > Title - max length is 255 characters ★
    > Category - foreign key to ArticleCategory, sets to NULL when deleted ★
    > Entry - text field ★ 
    > Created On - datetime field, only gets set when the model is created ★
    > Updated On - datetime field, always updates on last model update ★
    > Articles should be sorted by the date it was created, in descending order ★
'''
# Create your models here.

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title