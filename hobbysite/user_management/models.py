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
    display_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    

    # default display_name is user.username
    def save(self, *args, **kwargs):
        if not self.display_name:
            self.display_name = self.user.username
        if not self.email:
            self.email = self.user.email
        super().save(*args, **kwargs)
