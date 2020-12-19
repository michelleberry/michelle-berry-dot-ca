import datetime

from django.db import models
from django.utils import timezone

class collection(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class artPiece(models.Model):
    belongsTo = models.ForeignKey(collection, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField()
    yearCreated = models.IntegerField(default=2020)
    medium = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")
    def __str__(self):
        return self.title

