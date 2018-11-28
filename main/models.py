from django.db import models
import uuid

class Country(models.Model):
    title = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title


class Container(models.Model):
    cid = models.CharField(unique=True, null=True, max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.cid

