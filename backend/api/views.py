from project.models import IdeasModel, PlayersModel, GameModel, WinnerModel
from rest_framework import viewsets
from project.serializers import IdeasSerializer, PlayersSerializer, GameSerializer, WinnerSerializer

# Create your views here.

class IdeasViewSet(viewsets.ModelViewSet):
    """
    API
    """
    queryset = IdeasModel.objects.all()
    serializer_class = IdeasSerializer

class PlayersViewSet(viewsets.ModelViewSet):
    queryset = PlayersModel.objects.all()
    serializer_class = PlayersSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = GameModel.objects.all()
    serializer_class = GameSerializer

class WinnerViewSet(viewsets.ModelViewSet):
    queryset = WinnerModel.objects.all()
    serializer_class = WinnerSerializer