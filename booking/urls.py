from rest_framework.routers import DefaultRouter
from .views import BookingViewset

router = DefaultRouter()
router.register('booking', BookingViewset, basename='booking')

urlpatterns = router.urls

    