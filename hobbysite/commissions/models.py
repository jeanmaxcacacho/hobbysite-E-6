from django.db import models

# Create your models here

class Commission(models.Model):
    STATUS_CHOICES = [
        ('O', 'Open'),
        ('F', 'Full'),
        ('C', 'Completed'),
        ('D', 'Discontinued')   
    ]
    title = models.CharField(max_length=2555)
    description = models.TextField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='O')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta: 
        ordering = ['created_on']

class Job(models.Model):
    role = models.TextField()
    people_required = models.IntegerField()
    commission = models.ForeignKey(
        'Commission',
        on_delete=models.CASCADE,
        related_name='commission'
    )

    def __str__(self):
        return self.role

class Job_Application(models.Model):
    applied_on=models.DateTimeField(auto_now_add=True),
    job_application = models.ForeignKey(
        'Job',
        on_delete=models.CASCADE,
        related_name='job_application'
    )

    


