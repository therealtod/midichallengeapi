from rest_framework import serializers
from apps.games.models import Question, Game
from apps.songs.serializers import SongSerializer
from apps.songs.models import Song


class QuestionSerializer(serializers.ModelSerializer):
    song = SongSerializer(read_only=True)
    song_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Question
        fields = ['song', 'suggestion', 'answer', 'song_id']

    def create(self, validated_data):
        song_id = validated_data.pop('song_id')
        song = Song.objects.get(pk=song_id)
        question = Question.objects.create(song=song, **validated_data)
        return question


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['player', 'game_type', 'score']
