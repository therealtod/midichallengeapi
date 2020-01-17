from rest_framework import viewsets
from apps.games.serializers import QuestionSerializer
from apps.games.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        # call the original 'list' to get the original response
        response = super(QuestionViewSet, self).list(request, *args, **kwargs) 

        # customize the response data
        response.data = {"questions": response.data} 

        # return response with this custom representation
        return response 
        