from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    titele = models.CharField(max_length=40)
    description = models.TextField()
    author = models.CharField(max_length=40, null=True)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @property
    def short_description(self):
        return self.description[:40] + '...'
