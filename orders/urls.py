from rest_framework import routers
from django.urls import path, include
from .views import PurchaseOrderViewSet, AcknowledgePurchaseOrderViewSet

router = routers.SimpleRouter()
router.register(r'', PurchaseOrderViewSet, basename='Order')
urlpatterns = router.urls
urlpatterns += [
    path('<int:pk>/acknowledge/', AcknowledgePurchaseOrderViewSet.as_view(
        {'post': 'create'}), name='acknowledge-order')
]
