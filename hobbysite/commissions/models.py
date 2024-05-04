from django.db import models

# Create your models here

class Commission(models.Model):
    COMMISSION_STATUS=[
        ('O', 'Open'),
        ('F', 'Full'),
        ('C', 'Completed'),
        ('D', 'Discontinued')   
    ]
    title = models.CharField(max_length=2555)
    description = models.TextField(max_length=255)
    status = models.CharField(max_length=1, choices=COMMISSION_STATUS, default='O')
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

class JobApplication(models.Model):
    APPLICATION_STATUS=[
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected')
    ]
    status=models.CharField(max_length=1, choices=APPLICATION_STATUS, default='P')
    applied_on=models.DateTimeField(auto_now_add=True)
    applicant=models.ForeignKey(
        'accounts.Profile',
        on_delete=models.CASCADE,
        related_name='applicant'
    )
    job = models.ForeignKey(
        'Job',
        on_delete=models.CASCADE,
        related_name='job'
    )

    def __str__(self):
        return self.status

    


