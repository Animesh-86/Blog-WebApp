from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # NOTE: For real login use Django's User model
    contact = models.CharField(max_length=15)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
