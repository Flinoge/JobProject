from rest_framework import serializers
from .models import IdeasModel

class IdeasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IdeasModel
        fields = ('__all__')