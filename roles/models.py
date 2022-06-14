from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from genres.models import Genre, Influence

# Create your models here.
class Role(models.Model):
    label = models.CharField(max_length=18)

class Group(models.Model):
    name = models.CharField(max_length=38)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    genres = models.ManyToManyField(Genre)
    influences = models.ManyToManyField(Influence)
    groups = models.ManyToManyField(Group, blank=True)
