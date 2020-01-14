from rest_framework import viewsets
from apps.games.serializers import QuestionSerializer, GameSerializer
from apps.games.models import Question, Game


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games entities to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer