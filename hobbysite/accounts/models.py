from django.db import models

# required fields of the profile model
# products bought
# products sold
# articles created (for wiki and blog)
# commissions created
# commissions joined

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
