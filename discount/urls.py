from rest_framework.routers import DefaultRouter
from .views import DiscountViewSet

router = DefaultRouter()
router.register('discount', DiscountViewSet, basename='discount')

urlpatterns = router.urls

    