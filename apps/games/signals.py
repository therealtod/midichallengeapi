from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from apps.games.models import MidiChallengePlayer


@receiver(post_save, sender=User)
def create_and_savemidichallenge_player(sender, instance, created, **kwargs):
    if created:
        MidiChallengePlayer.objects.get_or_create(user=instance)
