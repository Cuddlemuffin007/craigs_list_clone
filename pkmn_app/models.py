from django.db import models


class City(models.Model):
    name = models.CharField(max_length=15)


class AccountProfile(models.Model):
    user = models.OneToOneField('auth.User')
    preferred_cities = models.ManyToManyField(City)

