from rest_framework.routers import DefaultRouter
from .views import PhotoViewSet,AlbumbViewSet, get_presigned_url, confirm_upload
from django.urls import path

router = DefaultRouter()
router.register('photo', PhotoViewSet, basename='photo')
router.register('albumb', AlbumbViewSet, basename='albumb')

urlpatterns = router.urls+ [
    path('get-presigned-url/', get_presigned_url, name='get_presigned_url'),
    path('confirm-upload/', confirm_upload, name='confirm_upload'),
]