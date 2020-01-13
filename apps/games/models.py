from django.db import models

from apps.songs.models import Song


class Question(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    suggestion = models.CharField(max_length=200)
    answer = models.CharField(max_length=50, default='Non lo so')


