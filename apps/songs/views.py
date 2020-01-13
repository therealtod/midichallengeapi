from rest_framework import viewsets
from apps.songs.serializers import SongSerializer
from apps.songs.models import Song


class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer