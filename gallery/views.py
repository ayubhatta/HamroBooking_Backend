from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponseBadRequest
from urllib.parse import quote_plus


from .models import Albumb, Photo
from .serializers import PhotoSerializer, AlbumbSerializer



import boto3

import uuid

class AlbumbViewSet(ModelViewSet):
    queryset = Albumb.objects.all()
    serializer_class = AlbumbSerializer
    permission_classes = [AllowAny]

class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [AllowAny]

def get_presigned_url(request):
    s3_client = boto3.client('s3',
                             aws_access_key_id="AKIAVJ5WIBK3RUVMVX6I",
                             aws_secret_access_key="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",
                            #  aws_secret_access_key = quote_plus("dLRLFsvvzZw29YAa+VV7kbCnZmOJQx4MlVhTVXuL"),
                            #  config=Config(signature_version='s3v4'),
                            #  signature_version='s3v4',
                             region_name="ap-south-1")
    album_id = request.GET.get('id')
    if album_id is None:
        return HttpResponseBadRequest('Parameter "album_id" is missing')

    bucket_name = 'hamro-booking-images'
    image_id = str(uuid.uuid4())

    object_key = f'{album_id}/{image_id}.jpg/'
    presigned_url = s3_client.generate_presigned_url('put_object',
                                                     Params={'Bucket': bucket_name,
                                                             'Key': object_key},
                                                     ExpiresIn=86400)  # Set the expiration time in seconds
    return JsonResponse({'presigned_url': presigned_url})

@api_view(['POST'])
@permission_classes([AllowAny])
def confirm_upload(request):
    serializer = PhotoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # return Response({
        #         'data': serializer.data,
        #         'message': 'Room created successfully'

        #     }, status = status.HTTP_201_CREATED)
        return JsonResponse({'message': 'File uploaded successfully'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


