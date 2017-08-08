from rest_framework import serializers
from .models import IdeasModel, PlayersModel, GameModel, WinnerModel

class IdeasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IdeasModel
        fields = ('__all__')

class PlayersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayersModel
        fields = ('__all__')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameModel
        fields = ('__all__')

class WinnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WinnerModel
        fields = ('__all__')