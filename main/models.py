from django.db import models
import uuid
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return str(self.user.id)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Country(models.Model):
    title = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title


class Container(models.Model):
    cid = models.CharField(unique=True, null=True, max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    departed = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.cid


class Booking(models.Model):
    bid = models.CharField(unique=True, null=True, max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    location = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    departure_date = models.DateTimeField(null=True, blank=True)
    arrival_date = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.container)

    def save(self, *args, **kwargs):
        if not self.id:
            self.bid = str(uuid.uuid4())
            super(Booking, self).save(*args, **kwargs)



