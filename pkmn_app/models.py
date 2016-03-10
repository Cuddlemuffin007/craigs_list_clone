from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class City(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class AccountProfile(models.Model):
    user = models.OneToOneField('auth.User')
    preferred_cities = models.ManyToManyField(City)


@receiver(post_save, sender='auth.User')
def create_account_profile(sender, **kwargs):
    user_instance = kwargs.get('instance')
    created = kwargs.get('created')
    if created:
        AccountProfile.objects.create(user=user_instance)