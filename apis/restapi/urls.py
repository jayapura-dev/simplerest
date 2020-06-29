from .views import DistrikViewset, KampungViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'distrik', DistrikViewset, basename='distrik')
router.register(r'kampung', KampungViewset, basename='kampung')

urlpatterns = router.urls