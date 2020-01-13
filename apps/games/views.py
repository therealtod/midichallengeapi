from rest_framework import viewsets
from apps.games.serializers import QuestionSerializer
from apps.games.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
