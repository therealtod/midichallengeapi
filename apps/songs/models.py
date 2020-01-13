from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=50)
    filename = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
