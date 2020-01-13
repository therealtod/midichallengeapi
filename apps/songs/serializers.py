from rest_framework import serializers

from apps.songs.models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'filename', 'author']
