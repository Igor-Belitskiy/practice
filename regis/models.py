from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #bio = models.TextField(min_value=5,max_length=500, blank=True)
    pass