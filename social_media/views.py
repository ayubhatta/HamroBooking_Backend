from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Social_media
from .serializers import SocialMediaSerializer

class SocialMediaViewSet(ModelViewSet):
    queryset = Social_media.objects.all()
    serializer_class = SocialMediaSerializer
    permission_classes = [AllowAny]
