from project.models import ExampleModel, LinkExample
from rest_framework import viewsets
from project.serializers import ExampleModelSerializer, LinkExampleSerializer

# Create your views here.

class ExampleModelViewSet(viewsets.ModelViewSet):
    """
    API
    """
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer

class LinkExampleViewSet(viewsets.ModelViewSet):
    """
    API
    """
    queryset = LinkExample.objects.all()
    serializer_class = LinkExampleSerializer
