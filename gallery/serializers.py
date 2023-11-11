from rest_framework import serializers

from .models import Albumb, Photo


class AlbumbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albumb
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"

