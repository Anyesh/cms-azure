from django.db import models
import uuid
from django.contrib.auth.models import User

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


class Booking(models.Model):
    bid = models.CharField(unique=True, null=True, max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    departure_date = models.DateTimeField(null=True, blank=True)
    arrival_date = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.container)

    def save(self, *args, **kwargs):
        if not self.id:
            self.bid = str(uuid.uuid4())
            super(Booking, self).save(*args, **kwargs)



