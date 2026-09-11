from django.conf import settings
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="questions",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    views = models.PositiveIntegerField(default=0)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title