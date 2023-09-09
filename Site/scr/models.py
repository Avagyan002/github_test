from django.db import models
from django.contrib.auth.models import User


class SiteUser(models.Model):
    gender_choice = [(1, 'Male'), (2, 'Female'), (3, 'Unknown')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    age = models.PositiveSmallIntegerField()
    gender = models.PositiveBigIntegerField(choices=gender_choice)