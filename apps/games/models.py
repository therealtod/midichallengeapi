from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.songs.models import Song

class MidiChallengePlayer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_midichallenge_player(sender, instance, created, **kwargs):
    if created:
        MidiChallengePlayer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_midichallenge_player(sender, instance, **kwargs):
    instance.profile.save()

class Question(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    suggestion = models.CharField(max_length=200)
    answer = models.CharField(max_length=50, default='Non lo so')


class Game(models.Model):
    class GameType(models.TextChoices):
        CLASSIC = 'C', _('Classic')
        TIME_ATTACK = 'T', _('Time Attack')
        BATTLE = 'B', _('Battle')

    game_type = models.CharField(max_length=20, choices=GameType.choices)
    player = models.ForeignKey(MidiChallengePlayer, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
