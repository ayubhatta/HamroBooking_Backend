from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Feature
from .serializers import FeatureSerializer

class FeatureViewSet(ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [AllowAny]

