from django.db import models
from django.contrib.auth.models import User

# required fields of the profile model
# products bought
# products sold
# articles created (for wiki and blog)
# commissions created
# commissions joined

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()


    def __str__(self):
        return self.user_name
