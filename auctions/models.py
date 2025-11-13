from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.IntegerField()
    url_link = models.ImageField()

    def __str__(self):
        return f"{self.title}: {self.description} for {self.starting_bid}"

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass
