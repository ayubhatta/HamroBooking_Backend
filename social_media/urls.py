from rest_framework.routers import DefaultRouter
from .views import SocialMediaViewSet

router = DefaultRouter()
router.register('', SocialMediaViewSet, basename='socialmedia')

urlpatterns = router.urls