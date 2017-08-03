from rest_framework import serializers
from .models import ExampleModel, LinkExample

class ExampleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ('__all__')

class LinkExampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LinkExample
        fields = ('__all__')