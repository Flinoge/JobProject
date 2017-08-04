from project.models import IdeasModel
from rest_framework import viewsets
from project.serializers import IdeasSerializer

# Create your views here.

class IdeasViewSet(viewsets.ModelViewSet):
    """
    API
    """
    queryset = IdeasModel.objects.all()
    serializer_class = IdeasSerializer
