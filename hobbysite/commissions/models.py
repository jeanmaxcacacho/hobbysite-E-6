from django.db import models

# Create your models here

class Commission(models.Model):
    title = models.CharField(max_length=2555)
    description = models.TextField(max_length=255)
    people_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta: 
        ordering = ['created_on']

class Comment(models.Model):
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    commission = models.ForeignKey(
        'Commission',
        on_delete=models.CASCADE,
        related_name='comment'
    )

    def __str__(self):
        return self.entry
    
    class Meta: 
        ordering = ['-created_on']
    


