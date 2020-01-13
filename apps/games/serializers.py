from rest_framework import serializers
from apps.games.models import Question
from apps.songs.serializers import SongSerializer


class QuestionSerializer(serializers.ModelSerializer):
    song = SongSerializer()

    class Meta:
        model = Question
        fields = ['song', 'suggestion', 'answer']
