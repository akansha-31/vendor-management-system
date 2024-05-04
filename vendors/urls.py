from rest_framework import routers
from .views import VendorViewSet

router = routers.SimpleRouter()
router.register(r'', VendorViewSet)
urlpatterns = router.urls
