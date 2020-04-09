from django.db import models


class Url(models.Model):
    title = models.CharField(max_length=128, blank=False)
    reference = models.CharField(max_length=256, blank=False)
    description = models.TextField()
    up = models.BooleanField(default=False)