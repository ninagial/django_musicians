from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Genre(models.Model):
    label = models.CharField(max_length=38)

class Influence(models.Model):
    label = models.CharField(max_length=38)
    genres = models.ManyToManyField(Genre, related_name='has_genres')
