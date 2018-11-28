from django.db import models
import uuid


class Container(models.Model):
    cid = models.CharField(unique=True, null=True, blank=True, max_length=200)
