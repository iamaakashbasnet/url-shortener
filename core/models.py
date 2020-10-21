import secrets
from django.db import models
from accounts.models import Account


def get_token():
    return secrets.token_urlsafe(4)


class Link(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    url = models.URLField(max_length=255)
    short_url = models.CharField(
        max_length=100, unique=True, default=get_token)

    def __str__(self):
        return f'{self.author} - {self.short_url}'

    @property
    def total_urls(self):
        return self.url.count()
