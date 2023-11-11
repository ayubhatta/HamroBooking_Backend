from rest_framework import serializers

from .models import Social_media


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_media
        fields = "__all__"