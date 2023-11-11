from rest_framework.routers import DefaultRouter
from .views import FeatureViewSet

router = DefaultRouter()
router.register('feature', FeatureViewSet, basename='feature')

urlpatterns = router.urls